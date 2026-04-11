#!/usr/bin/env python3
"""Concurrent coroutines: collect wait_random delays in ascending completion order."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Spawn wait_random n times; return delays ascending (order of completion, no sort)."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await coro for coro in asyncio.as_completed(tasks)]
