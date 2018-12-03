#!/usr/bin/env python

# This file is part of asynckrakenex.
# Licensed under the Simplified BSD license. See `examples/LICENSE.txt`.

# Prints the account blance to standard output.

import asynckrakenex

k = asynckrakenex.API()
k.load_key('kraken.key')

print(k.query_private('Balance'))
