#!/usr/bin/env python3

from numbers import Number
import ezocalc.bloc
import ezocalc.operand
import ezocalc.value

class Operation(ezocalc.bloc.Bloc):

    _blocs = None

    def __init__(self):
        self._blocs = []

    def append(self, b:ezocalc.bloc.Bloc):
        self._blocs.append(b)

    def get_value(self) -> Number:
        """Returns value of the bloc (direct value or calculation)"""

        (pos, ope) = self._find_ope()
        while pos > 0:
            val = ope.calculate(self._blocs[pos-1], self._blocs[pos+1])
            self._blocs[pos-1] = ezocalc.value.Value(val)
            del self._blocs[pos:pos+2]

            (pos, ope) = self._find_ope()

        return self._blocs[0].get_value()


    def _find_ope(self):
        pos = 0
        for e in self._blocs:
            if type(e) is ezocalc.operand.Operand and e.is_first():
                return (pos, e)
            pos += 1

        pos = 0
        for e in self._blocs:
            if type(e) is ezocalc.operand.Operand and e.is_second():
                return (pos, e)
            pos += 1

        pos = 0
        for e in self._blocs:
            if type(e) is ezocalc.operand.Operand:
                return (pos, e)
            pos += 1

        return (-1, None)
