#!/usr/bin/env python

# This file is part of asynckrakenex.
# Licensed under the Simplified BSD license. See `examples/LICENSE.txt`.

# Get balance available for trading/withdrawal (not on orders).
#
# NOTE: Assumes regular orders. Margin positions are not taken into account!
#
# FIXME: Also shows how current asynckrakenex usage has too much sugar.

import asyncio
from decimal import Decimal as Dec

import asynckrakenex


async def print_available_balances():
    k = asynckrakenex.API()
    k.load_key('test-kraken.key')

    balance = await k.query_private('Balance')
    orders = await k.query_private('OpenOrders')

    balance = balance['result']
    orders = orders['result']

    new_balance = dict()
    for currency in balance:
        # remove first symbol ('Z' or 'X'), but not for GNO or DASH
        new_name = currency[1:] if len(currency) == 4 and currency != "DASH" else currency
        new_balance[new_name] = Dec(balance[currency])  # type(balance[currency]) == str
    balance = new_balance

    for _, o in orders['open'].items():
        # remaining volume in base currency
        volume = Dec(o['vol']) - Dec(o['vol_exec'])

        # extract for less typing
        descr = o['descr']

        # order price
        price = Dec(descr['price'])

        pair = descr['pair']
        base = pair[:3] if pair != "DASHEUR" else "DASH"
        quote = pair[3:] if pair != "DASHEUR" else "EUR"

        type_ = descr['type']
        if type_ == 'buy':
            # buying for quote - reduce quote balance
            balance[quote] -= volume * price
        elif type_ == 'sell':
            # selling base - reduce base balance
            balance[base] -= volume

    for k, v in balance.items():
        # convert to string for printing
        if v == Dec('0'):
            s = '0'
        else:
            s = str(v)
        # remove trailing zeros (remnant of being decimal)
        s = s.rstrip('0').rstrip('.') if '.' in s else s
        #
        print(k, s)


loop = asyncio.get_event_loop()
loop.run_until_complete(print_available_balances())
