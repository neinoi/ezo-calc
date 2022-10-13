#!/usr/bin/env python3

from numbers import Number

class Bloc:

    def get_value(self) -> Number:
        """Returns value of the bloc (direct value or calculation)"""
        pass

    def is_operand(self):
        return False