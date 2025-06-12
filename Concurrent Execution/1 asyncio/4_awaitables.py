"""Awaitables
We say that an object is an awaitable object if it can be used in an await expression.
Many asyncio APIs are designed to accept awaitables.

There are three main types of awaitable objects:
    Coroutines, Tasks, and Futures.

Terms:
    a coroutine function: an async def function;
    a coroutine object: an object returned by calling a coroutine function.
"""

import asyncio

async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()  # will raise a "RuntimeWarning".

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())
