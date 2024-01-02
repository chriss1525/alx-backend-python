#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""alter wait_n function with asyncio.gather"""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """return the list of all the delays (float values)."""
    list_delays = []
    for i in range(n):
        list_delays.append(asyncio.create_task(wait_random(max_delay)))
    return [await delay for delay in asyncio.as_completed(list_delays)]
