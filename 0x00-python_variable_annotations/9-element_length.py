#!/usr/bin/env python3
"""
9. Let's duck type an iterable object
"""
from typing import List, Sequence, Tuple


def element_length(lst: List[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
