import gevent
from gevent.queue import Queue

def func():
    for i in range(10):
        print('in the func()')
        q.put("test")
        gevent.sleep(0)

def func2():
    for i in range(10):
        print('in the func2()')
        res = q.get()
        print("--->", res)

q = Queue()

gevent.joinall(
    [
        gevent.spawn(func2),
        gevent.spawn(func),
    ]
)