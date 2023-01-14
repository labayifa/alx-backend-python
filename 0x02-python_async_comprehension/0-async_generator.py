#!/usr/bin/env python3
"""
0. Async Generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    :return: List of float value
    """
    i: int = 0
    while i != 10:
        i += 1
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
