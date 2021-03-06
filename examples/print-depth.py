#!/usr/bin/env python3

# This file is part of async-krakenex.
# Licensed under the Simplified BSD license. See `examples/LICENSE.txt`.

# Pretty-print a pair's order book depth.

from requests.exceptions import HTTPError

import asynckrakenex
import asyncio

import pprint


async def print_depth():
    kraken = asynckrakenex.API()
    try:
        response = await kraken.query_public('Depth', {'pair': 'XXBTZUSD', 'count': '10'})
        pprint.pprint(response)
    except HTTPError as e:
        print(str(e))
    finally:
        await kraken.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(print_depth())
