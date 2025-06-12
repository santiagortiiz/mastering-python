"""There are 3 methods to start a process:
-spawn: starts a fresh Python interpreter process
-fork: uses os.fork() to fork the Python interpreter
-forkserver: a server process is spawned. From then on,
    whenever a new process is needed, the parent process
    connects to the server and requests that it fork a new process.
    The fork server process is single threaded unless system
    libraries or preloaded imports spawn threads as a side-effect
    so it is generally safe for it to use os.fork().
    No unnecessary resources are inherited.

On POSIX using the spawn or forkserver start methods will also start
a resource tracker process which tracks the unlinked named system
resources (such as named semaphores or SharedMemory objects)

(Neither leaked semaphores nor shared memory segments will be automatically
unlinked until the next reboot. This is problematic for both objects because
the system allows only a limited number of named semaphores, and shared
memory segments occupy some space in the main memory.)
"""

import multiprocessing as mp

def foo(queue: mp.Queue):
    queue.put('hello')

if __name__ == '__main__':
    # set_start_method should not be used more than once in the program.
    mp.set_start_method('spawn')

    q: mp.Queue = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()
