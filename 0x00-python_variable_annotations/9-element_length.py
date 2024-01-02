#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" annotate function's parameter and return value"""

from typing import List, Sequence, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return a list of tuples where each tuple contains
    a sequence and its length"""
    return [(seq, len(seq)) for seq in lst]
