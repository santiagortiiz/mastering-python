"""Exchanging objects between processes.

The Pipe() function returns a pair of connection objects connected by a pipe,
which by default is duplex (two-way)

data in a pipe may become corrupted if two processes (or threads) try to
read from or write to the same end of the pipe at the same time
"""
from multiprocessing import Process, Pipe

from utils.cpu_intensive import cpu_intensive_operation


def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    p.join()