#!/usr/bin/env python3
"""
0. The basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    :param max_delay:
    :return:
    """
    delay = random.uniform(0, max_delay)
    return await asyncio.sleep(delay, delay)
