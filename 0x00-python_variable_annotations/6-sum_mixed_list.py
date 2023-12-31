#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" function that takes a list with mixed types (integers and strings)
and returns the sum of the values that can be converted to integers."""

import math
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ function that takes a list with mixed types (integers and strings)
    and returns the sum of the values that can be converted to integers."""
    return (sum(mxd_lst))
