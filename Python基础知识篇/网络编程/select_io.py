import  select
import types
import collections


class Task(Object):

    def __init__(self, target):
        self.target = target
        self.sendval = None
        self.stack = []

    def run(self):
        try:
            result = self.target.send(self.sendval)
            if isinstance(result, SystemCall):
                return result
            if isinstance(result, types.GeneratorType):
                self.stack.append(self.target)
                self.sendval = None
                self.target = result
            else:
                if not self.stack: return
                self.sendval = result
                self.target = self.stack.pop()
        except StopIteration as e:
            if not self.stack: raise
            self.sendval = None
            self.target = self.stack.pop()


class SystemCall(object):
    def hand(self, sched, task):
        pass


class Scheduler(object):
    def __init__(self):
        self.task_queue = collections.deque()
        self.read_waiting = {}
        self.write_waiting = {}
        self.numtasks = 0

    def new(self, target):
        newtask = Task(target)
        self.schedule(newtask)
        self.numtasks += 1

    def schedule(self, task):
        self.task_queue.append(task)

    def readwait(self, task, fd):
        self.read_waiting[fd] = task

    def writewait(self, task, fd):
        self.write_waiting[fd] = task

    def mainloop(self, conut=-1, timeout=None):
        while self.numtasks:
            if self.read_waiting or self.write_waiting:
                wait = 0 if self.task_queue else timeout
                r, w, e = select.select(self.read_waiting, self.write_waiting, [], wait)

                for fileno in r:
                    self.schedule(self.read_waiting.pop[fileno])

                for fileno in w:
                    self.schedule(self.write_waiting.pop(fileno))

            while self.task_queue:
                task = self.task_queue.popleft()
                try:
                    result = task.run()
                    if isinstance(result.SystemCall):
                        result.handle(self, task)
                    else:
                        self.schedule(task)
                except StopIteration as e:
                    self.numtasks -= 1

            else:
                if conut >0: count -= 1
                if count == 0:
                    return
