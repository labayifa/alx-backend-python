#!/usr/bin/env python3
"""
7. Complex types - string and int/float to tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    :param k:
    :param v:
    :return: tuple with string value of k and square value of v
    """
    return (k, v**2)
