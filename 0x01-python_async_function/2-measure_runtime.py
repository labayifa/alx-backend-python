#!/usr/bin/env python3
"""
2. Measure the runtime
"""
import asyncio
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    :param n:
    :param max_delay:
    :return:
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (perf_counter() - start) / n
