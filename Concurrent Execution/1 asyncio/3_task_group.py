import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

# The first time any of the tasks belonging to the group fails with an
# exception other than asyncio.CancelledError, the remaining tasks in the
# group are cancelled.
# async def say_after_2(delay, what):
#     raise ValueError("hola")
#     await asyncio.sleep(delay)
#     print(what)

async def main():
    """The timing and output should be the same as for the previous version."""
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(1, 'hello'))

        task2 = tg.create_task(
            say_after(2, 'world'))

        print(f"started at {time.strftime('%X')}")

    # The await is implicit when the context manager exits.

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
