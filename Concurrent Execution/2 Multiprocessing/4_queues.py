"""Exchanging objects between processes"""
from multiprocessing import Process, Queue

from utils.cpu_intensive import cpu_intensive_operation

def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    # p = Process(target=f, args=(q,))
    p = Process(target=cpu_intensive_operation, args=(100000, q))
    print("Spawning child process with intensive cpu operations...")
    p.start()
    print("Doing other operations in the parent process...")
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()
