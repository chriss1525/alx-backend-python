#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""validate code using mypy"""

from typing import List, Tuple

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """validate code using mypy"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

arr = [12, 72, 91]
zoom_2x = zoom_array(arr)
zoom_3x = zoom_array(arr, 3.0)
