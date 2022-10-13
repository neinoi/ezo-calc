#!/usr/bin/env python3

import mapper
import sys
import argparse

calculator = mapper.Mapper()

if __name__ == "__main__":

    calcul = ' '.join(sys.argv[1:])

    print("CALCUL : ", calcul)

    calc_tree = calculator.scan(calcul)

    print("RESULT :", calc_tree.get_value())
