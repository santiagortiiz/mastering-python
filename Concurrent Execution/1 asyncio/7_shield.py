"""Protect an awaitable object from being cancelled.

if the coroutine containing it is cancelled, the Task running in something()
is not cancelled. From the point of view of something(), the cancellation did
not happen. Although its caller is still cancelled, so the “await” expression
still raises a CancelledError.

If something() is cancelled by other means (i.e. from within itself) that would
also cancel shield().
"""

import asyncio
from asyncio import shield

task = asyncio.create_task(something())
res = await shield(task)

# If it is desired to completely ignore cancellation (not recommended) the
# shield() function should be combined with a try/except clause, as follows:
task = asyncio.create_task(something())
try:
    res = await shield(task)
except CancelledError:
    res = None
