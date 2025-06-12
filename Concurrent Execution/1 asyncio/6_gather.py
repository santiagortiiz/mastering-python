import asyncio

from utils import cpu_work

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    """Schedule three calls *concurrently*
    A common example where this is beneficial is coroutines which employ
    caching or memoization to avoid actual I/O when possible.
    """
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
        # cpu_work(3),
        # cpu_work(1),
        # cpu_work(5),
    )
    print("hello")
    print(L)
    print("world")

asyncio.run(main())
