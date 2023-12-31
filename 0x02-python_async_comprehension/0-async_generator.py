#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" coroutine command that takes no arguments."""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ coroutine command that takes no arguments."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
