#!/usr/bin/env python3
"""
9. Let's duck type an iterable object
"""
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    :param lst:
    :return:  values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
