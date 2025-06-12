"""Important
Save a reference to the result of this function, to avoid a task
disappearing mid-execution. The event loop only keeps weak references to tasks.
A task that isn't referenced elsewhere may get garbage collected at any time,
even before it's done. For reliable “fire-and-forget” background tasks, gather
them in a collection:
"""
import asyncio

background_tasks = set()

for i in range(10):
    task = asyncio.create_task(some_coro(param=i))

    # Add task to the set. This creates a strong reference.
    background_tasks.add(task)

    # To prevent keeping references to finished tasks forever,
    # make each task remove its own reference from the set after
    # completion:
    task.add_done_callback(background_tasks.discard)
