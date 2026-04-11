#!/usr/bin/env python3
"""Sum a list of ints and floats with type annotations."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of all numbers in mxd_lst."""
    return float(sum(mxd_lst))
