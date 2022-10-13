#!/usr/bin/env python3
import decimal
from numbers import Number
import ezocalc.bloc


class Operand(ezocalc.bloc.Bloc):

    _opcode = None

    def __init__(self, operation):
        self._opcode = operation

    def calculate(self, left: ezocalc.bloc.Bloc, right: ezocalc.bloc.Bloc) -> Number:
        if self._opcode == '+':
            return left.get_value() + right.get_value()
        elif self._opcode == '-':
            return left.get_value() - right.get_value()
        elif self._opcode == '*':
            return left.get_value() * right.get_value()
        elif self._opcode == '/':
            return left.get_value() / right.get_value()
        elif self._opcode == '^':
            return left.get_value() ** right.get_value()

    def is_first(self):
        return self._opcode in ['^']

    def is_second(self):
        return self._opcode in ['*','/']


    def is_operand(self):
        return True