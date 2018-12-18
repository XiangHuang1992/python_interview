import multiprocessing
import time


class CloackProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        while True:
            print("the time is %s" % time.ctime())
            time.sleep(self.interval)

# def clock(interval):
#     while True:
#         print("the time is %s" % time.ctime())
#         time.sleep(interval)

if __name__ == '__main__':
    # p = multiprocessing.Process(target=clock, args=(3,))
    # p.start()
    p = CloackProcess(3)
    p.start()
