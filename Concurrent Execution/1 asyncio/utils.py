async def cpu_work(work_units: int):
    """This func. simulates a CPU intensive operation, that will
    keep the processor bussy for a period of time.
    """
    x = 0
    for _ in range(work_units * 1_000_000):
        x += 1

    return x
