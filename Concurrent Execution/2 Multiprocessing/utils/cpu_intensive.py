
from multiprocessing import Queue
import time
from typing import Union

from .info import log_process_info

def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

def cpu_intensive_operation(n, q: Union[Queue, None] = None):
    # log_process_info()

    inicio = time.time()
    factorial = calcular_factorial(n)
    fin = time.time()
    elapsed_time = f"{fin - inicio:.4f}"
    print(f"Factorial de {n} calculado en {elapsed_time} segundos.")

    if q:
        q.put(elapsed_time)
    else:
        return elapsed_time


# Ejemplo de uso
if __name__ == "__main__":
    NUMERO = 1000  # Puedes ajustar este número para hacer la operación más o menos intensiva
    tiempo, factorial = cpu_intensive_operation(NUMERO)
    print(f"Factorial de {NUMERO} calculado en {tiempo} segundos.")
