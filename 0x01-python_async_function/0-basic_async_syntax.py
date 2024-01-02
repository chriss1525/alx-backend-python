#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# asynchronous coroutine that takes in an integer argument

"""Asynchronous coroutine"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine"""
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
