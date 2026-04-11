#!/usr/bin/env python3
"""Pairs of sequences and their lengths with type annotations."""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of (element, len(element)) for each item in lst."""
    return [(i, len(i)) for i in lst]
