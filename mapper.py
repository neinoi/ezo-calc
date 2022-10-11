#!/usr/bin/env python3

import operand
import operation
import value

OPERATORS = ['*','/','+','-','^']

class Mapper():
    _operation: operation.Operation

    def __init__(self):
        self._operation = operation.Operation()

    def scan(self, expression:str):
        expression = expression.strip().replace(",", ".")

        while expression.find('(') != -1:
            # maps first elements
            if expression.find('(') > 0:
                self._map_simple(expression[0:expression.find('(')])
                expression = expression[expression.find('('):]

            # must find corresponding closing
            pos_end = expression.find(')')
            count_open = expression[:pos_end].count('(')
            count_close = 1
            while count_open != count_close:
                pos_end = expression.find(')',pos_end+1)
                count_open = expression[:pos_end].count('(')
                count_close += 1

            mapper = Mapper()
            self._operation.append(mapper.scan(expression[1: pos_end]))

            expression = expression[pos_end+1:]

        # remaining mapping
        if len(expression.strip()) > 0:
            self._map_simple(expression)

        return self._operation

    def _map_simple(self, sub):
        splits = sub.strip().split(' ')

        for s in splits:
            if s in OPERATORS:
                self._operation.append(operand.Operand(s))
            elif '^' in s:
                self._map_expo(s)
            else:
                self._operation.append(value.Value(s))

    def _map_expo(self, expo):

        expression = expo

        if expression.find('^') > 0:
            expo_ope = operation.Operation()
            if expression[0] == '-':
                expo_ope.append(value.Value('-1'))
                expo_ope.append(operand.Operand('*'))
                expression = expo[1:]

            expo_ope.append(value.Value(expression[:expression.find('^')]))

            expo_ope.append(operand.Operand('^'))

            if expression.find('^') < (len(expression)-1):
                expo_ope.append(value.Value(expression[expression.find('^')+1:]))

            self._operation.append(expo_ope)
        else:
            self._operation.append(operand.Operand('^'))

            if expression.find('^') < len(expression):
                self._operation.append(value.Value(expression[expression.find('^')+1:]))
