#!/usr/bin/env python3

from numbers import Number
from decimal import *
import bloc


class Value(bloc.Bloc):

    _value: Decimal

    def __init__(self, value):
        self._value = Decimal(value)

    def get_value(self) -> Number:
        return self._value