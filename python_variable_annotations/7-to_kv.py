#!/usr/bin/env python3
"""Build a key and squared value tuple with type annotations."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of k and the square of v."""
    return (k, v ** 2)
