#!/usr/bin/env python

# This file is part of asynckrakenex.
# Licensed under the Simplified BSD license. See `examples/LICENSE.txt`.

# Prints the account blance to standard output.

import asynckrakenex
import asyncio


async def print_account_balance():
    async with asynckrakenex.API.from_filename('test-kraken.key') as k:
        p = await k.query_private('Balance')
        print(p)


loop = asyncio.get_event_loop()
loop.run_until_complete(print_account_balance())
