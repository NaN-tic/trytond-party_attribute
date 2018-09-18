#!/usr/bin/env python
# This file is part of the party_attribute module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import party

def register():
    Pool.register(
        party.PartyAttributeSet,
        party.PartyAttribute,
        party.PartyAttributeAttributeSet,
        party.Party,
        module='party_attribute', type_='model')
