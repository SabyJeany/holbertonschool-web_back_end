#!/usr/bin/env python3
"""Run multiple wait_random coroutines concurrently."""

import asyncio
import heapq

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Spawn n concurrent wait_random(max_delay) calls; return delays ascending."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return heapq.nsmallest(len(delays), delays)
