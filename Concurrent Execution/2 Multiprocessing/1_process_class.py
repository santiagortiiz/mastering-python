from multiprocessing import Process

from utils.cpu_intensive import cpu_intensive_operation
from utils.info import log_process_info


def f(name):
    print('hello', name)

if __name__ == '__main__':
    log_process_info()
    p2 = Process(target=f, args=("santiago",))
    p = Process(target=cpu_intensive_operation, args=(1000,))
    p.start()
    p.join()
