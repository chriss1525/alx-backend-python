#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""import previous wait_random function and write an async routine"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay: int) -> List[float]:
    """return list of awaited responses"""
    res = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )

    return sorted(res)
