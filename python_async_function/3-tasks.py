#!/usr/bin/env python3
"""Schedule wait_random as an asyncio.Task."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return a Task that runs wait_random(max_delay)."""
    return asyncio.create_task(wait_random(max_delay))
