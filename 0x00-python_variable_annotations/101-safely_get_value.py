#!/usr/bin/env python3
"""
11. More involved type annotations
"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, Any] = None) -> Union[Any, T]:
    """
    :param dct:
    :param key:
    :param default:
    :return: defalut value if key not found or key value if found
    """
    if key in dct:
        return dct[key]
    else:
        return default
