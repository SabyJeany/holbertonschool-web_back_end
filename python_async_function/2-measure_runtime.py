#!/usr/bin/env python3
"""Measure average wall-clock time per task for wait_n."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Run wait_n(n, max_delay) and return total elapsed time divided by n."""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start
    return elapsed / n
