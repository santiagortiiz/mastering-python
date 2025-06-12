"""si el módulo multriprocessing ya me permite hacer eso, en que caso debería considerar usar get_context?

Note that objects related to one context may not be compatible with processes for a different context.
In particular, locks created using the fork context cannot be passed to processes
started using the spawn or forkserver start methods.

A library which wants to use a particular start method should probably use get_context()
to avoid interfering with the choice of the library user.
"""
import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()
