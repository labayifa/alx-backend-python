#!/usr/bin/env python3
"""
3. Tasks
"""
import asyncio
from asyncio import Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    :param max_delay:
    :return:
    """
    return asyncio.create_task(wait_random(max_delay))
