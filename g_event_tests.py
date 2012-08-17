# import gevent
# import random

# def task(pid):
#     """
#     Some non-deterministic task
#     """
#     gevent.sleep(random.randint(0,2)*0.001)
#     print('Task', pid, 'done')

# def synchronous():
#     for i in range(1,10):
#         task(i)

# def asynchronous():
#     threads = [gevent.spawn(task, i) for i in xrange(10)]
#     gevent.joinall(threads)

# print('Synchronous:')
# synchronous()

# print('Asynchronous:')
# asynchronous()





# import gevent

# def foo():
#     print('Running in foo and then will go to sleep.')
#     gevent.sleep(0)
#     print('Explicit context switch to foo again')

# def bar():
#     print('Explicit context to bar')
#     gevent.sleep(0)
#     print('Implicit context switch back to bar')

# gevent.joinall([
#     gevent.spawn(foo),
#     gevent.spawn(bar),
# ])

import time
import gevent
from gevent import select

start = time.time()
tic = lambda: 'at %1.1f seconds' % (time.time() - start)

def gr1():
    # Busy waits for a second, but we don't want to stick around...
    print('Started Polling: ', tic())
    select.select([], [], [], 2)
    print('Ended Polling: ', tic())

def gr2():
    # Busy waits for a second, but we don't want to stick around...
    print('Started Polling: ', tic())
    select.select([], [], [], 2)
    print('Ended Polling: ', tic())

def gr3():
    print("Hey lets do some stuff while the greenlets poll, at", tic())
    gevent.sleep(1)

gevent.joinall([
    gevent.spawn(gr1),
    gevent.spawn(gr2),
    gevent.spawn(gr3),
])