import os

def log_process_info():
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
