#!/usr/bin/env python
# This file is part of the party_attribute module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, DictSchemaMixin, fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__metaclass__ = PoolMeta
__all__ = ['PartyAttributeSet', 'PartyAttribute',
    'PartyAttributeAttributeSet', 'Party']


class PartyAttributeSet(ModelSQL, ModelView):
    "Party Attribute Set"
    __name__ = 'party.attribute.set'
    name = fields.Char('Name', required=True, translate=True)
    attributes = fields.Many2Many('party.attribute-party.attribute-set',
        'attribute_set', 'attribute', 'Attributes')


class PartyAttribute(DictSchemaMixin, ModelSQL, ModelView):
    "Party Attribute"
    __name__ = 'party.attribute'
    sets = fields.Many2Many('party.attribute-party.attribute-set',
        'attribute', 'attribute_set', 'Sets')


class PartyAttributeAttributeSet(ModelSQL):
    "Party Attribute - Set"
    __name__ = 'party.attribute-party.attribute-set'
    attribute = fields.Many2One('party.attribute', 'Attribute',
        ondelete='CASCADE', select=True, required=True)
    attribute_set = fields.Many2One('party.attribute.set', 'Set',
        ondelete='CASCADE', select=True, required=True)


class Party:
    __name__ = 'party.party'
    attribute_set = fields.Many2One('party.attribute.set', 'Set')
    attributes = fields.Dict('party.attribute', 'Attributes',
        domain=[
            ('sets', '=', Eval('attribute_set', -1)),
            ],
        states={
            'readonly': ~Eval('attribute_set'),
            },
        depends=['attribute_set'])
