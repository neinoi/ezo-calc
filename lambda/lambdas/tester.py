#!/usr/bin/env python3

import ezocalc.mapper

calculator = ezocalc.mapper.Mapper()

if __name__ == "__main__":

    calcul = "1+10^(9/4)"

    print("CALCUL : ", calcul)

    calc_tree = calculator.scan(calcul)

    print("RESULT :", calc_tree.get_value())
