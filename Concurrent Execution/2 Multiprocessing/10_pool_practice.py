from multiprocessing import Pool, TimeoutError
import time

from utils.cpu_intensive import cpu_intensive_operation

if __name__ == '__main__':
    # start 4 worker processes
    WORKERS = 4
    inicio = time.time()

    with Pool(processes=WORKERS) as pool:
        # launching multiple evaluations asynchronously *may* use more processes
        multiple_results = [pool.apply_async(cpu_intensive_operation, (i, )) for i in range(10000, 100000, 20000)]
        print("Parent process doing more things while children finish CPU intensive operations...\n")
        print([res.get() for res in multiple_results])

    fin = time.time()
    print(f"Workers: {WORKERS} - time: {fin - inicio:.4f} seconds.")