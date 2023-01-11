#!/usr/bin/env python3
"""
4. Tasks
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    :param n:
    :param max_delay:
    :return: return the ordered list following time used
             to complete each task from tas list
    """
    tasks = [task_wait_random(max_delay) for i in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
