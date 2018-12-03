#!/usr/bin/env python3

# This file is part of asynckrakenex.
# Licensed under the Simplified BSD license. See `examples/LICENSE.txt`.

# Demonstrate use of json_options().

from types import SimpleNamespace

import asynckrakenex

kraken = asynckrakenex.API().json_options(object_hook=lambda kv: SimpleNamespace(**kv))
response = kraken.query_public('Time')

if response.error:
    print('error:', response.error)
else:
    result = response.result
    print('unixtime:', result.unixtime)
    print('rfc1123:', result.rfc1123)

