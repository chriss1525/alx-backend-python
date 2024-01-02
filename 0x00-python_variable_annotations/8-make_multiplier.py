#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" annotated function make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ annotated function make_multiplier"""
    def multiply(number: float) -> float:
        """ annotated function make_multiplier"""
        return number * multiplier
    return multiply
