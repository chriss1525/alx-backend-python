#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""add type annotation to function"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')
result = Union[Any, T]
DEFAULT = Union[T, None]

def safely_get_value(dct: Mapping, key: Any, default: DEFAULT = None) -> result:
    """add type annotation to function"""
    if key in dct:
        return dct[key]
    else:
        return default
