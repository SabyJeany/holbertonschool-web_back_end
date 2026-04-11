#!/usr/bin/env python3
"""Sum a list of floats with type annotations."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of all floats in input_list."""
    return float(sum(input_list))
