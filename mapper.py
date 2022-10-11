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
        expression = expression.strip().replace(",", ".").replace(" ","")

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
        splits = []
        acc = ""
        for l in sub:
            if l in OPERATORS:
                add_ope = True
                if len(acc) > 0:
                    splits.append(value.Value(acc))
                    acc = ""
                elif len(splits)>0 and splits[len(splits)-1].is_operand() and l != '-':
                    raise SyntaxError()
                elif ((len(splits)>0 and splits[len(splits)-1].is_operand()) or len(splits) == 0) and l == '-':
                    acc += "-"
                    add_ope = False

                if add_ope:
                    splits.append(operand.Operand(l))
            else:
                acc += l

        if len(acc) > 0:
            splits.append(value.Value(acc))

        for b in splits:
            self._operation.append(b)
