"""
Lock to ensure that only one process prints to standard output at a time:
"""
from multiprocessing import Process, Lock

def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

    # Try without lock:
    # print('WITHOUT: hello world', i)

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()