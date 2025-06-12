"""Server process

A manager object returned by Manager() controls a server process
which holds Python objects and allows other processes to manipulate
them using proxies.

Using a remote manager
It is possible to run a manager server on one machine and have clients
use it from other machines (assuming that the firewalls involved allow it).

"""
from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        # Child process that updates the dictionary "d"
        # which is shared with the main process.
        p = Process(target=f, args=(d, l))
        p.start()
        p.join()

        # Main process can see the updates made by its child
        print(d)
        print(l)
