#!/usr/bin/env python3

from numbers import Number
from decimal import *
import ezocalc.bloc


class Value(ezocalc.bloc.Bloc):

    _value: Decimal

    def __init__(self, value):
        try:
            self._value = Decimal(value)
        except InvalidOperation:
            raise SyntaxError(f'Invalid value : {value}')

    def get_value(self) -> Number:
        return self._value