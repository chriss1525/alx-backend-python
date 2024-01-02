#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""measure the total execution time for wait_n(n, max_delay)"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measure total execution time"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = (time.time() - start)/n
    return end
