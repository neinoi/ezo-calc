#!/usr/bin/env python3
import decimal
import unittest
import mapper
from decimal import *

class TestSum(unittest.TestCase):

    def test_01(self):
        calcul = "1 + 1"
        calcmap = mapper.Mapper()

        print("CALCUL : ", calcul)

        calc_tree = calcmap.scan(calcul)

        self.assertEqual(calc_tree.get_value(), 2)

    def test_02(self):
        calcul = "1 + 2"
        calcmap = mapper.Mapper()

        print("CALCUL : ", calcul)

        calc_tree = calcmap.scan(calcul)

        self.assertEqual(calc_tree.get_value(), 3)

    def test_03(self):
        calcul = "1 + -1"
        calcmap = mapper.Mapper()

        print("CALCUL : ", calcul)

        calc_tree = calcmap.scan(calcul)

        self.assertEqual(calc_tree.get_value(), 0)

    def test_04(self):
        calcul = "-1 - -1"
        calcmap = mapper.Mapper()

        print("CALCUL : ", calcul)

        calc_tree = calcmap.scan(calcul)

        self.assertEqual(calc_tree.get_value(), 0)

    def test_05(self):
        calcul = "5 - 4"
        calcmap = mapper.Mapper()

        print("CALCUL : ", calcul)

        calc_tree = calcmap.scan(calcul)

        self.assertEqual(calc_tree.get_value(), 1)

    def test_06(self):
        calcul = "5 * 2"
        calcmap = mapper.Mapper()

        print("CALCUL : ", calcul)

        calc_tree = calcmap.scan(calcul)

        self.assertEqual(calc_tree.get_value(), 10)

    def test_07(self):
        calcul = "(2 + 5) * 3"
        calcmap = mapper.Mapper()

        print("CALCUL : ", calcul)

        calc_tree = calcmap.scan(calcul)

        self.assertEqual(calc_tree.get_value(), 21)

    def test_08(self):
        calcul = "10 / 2"
        calcmap = mapper.Mapper()

        print("CALCUL : ", calcul)

        calc_tree = calcmap.scan(calcul)

        self.assertEqual(calc_tree.get_value(), 5)

    def test_09(self):
        calcul = "2 + 2 * 5 + 5"
        calcmap = mapper.Mapper()

        print("CALCUL : ", calcul)

        calc_tree = calcmap.scan(calcul)

        self.assertEqual(calc_tree.get_value(), 17)

    def test_10(self):
        calcul = "2.8 * 3 - 1"
        calcmap = mapper.Mapper()

        print("CALCUL : ", calcul)

        calc_tree = calcmap.scan(calcul)

        self.assertAlmostEqual(float(calc_tree.get_value()), 7.4)

    def test_11(self):
        calcul = "2^8"
        calcmap = mapper.Mapper()

        print("CALCUL : ", calcul)

        calc_tree = calcmap.scan(calcul)

        self.assertEqual(calc_tree.get_value(), 256)

    def test_12(self):
        calcul = "2^8 * 5 - 1"
        calcmap = mapper.Mapper()

        print("CALCUL : ", calcul)

        calc_tree = calcmap.scan(calcul)

        self.assertEqual(calc_tree.get_value(), 1279)

    def test_13a(self):
        # sqrt non implementee
        # calcul = "sqrt(4)"
        calcul = "4^(1/2)"
        calcmap = mapper.Mapper()

        print("CALCUL : ", calcul)

        calc_tree = calcmap.scan(calcul)

        self.assertEqual(calc_tree.get_value(), 2)

    def test_13b(self):
        calcul = "4 ^ (1 / 2)"
        calcmap = mapper.Mapper()

        print("CALCUL : ", calcul)

        calc_tree = calcmap.scan(calcul)

        self.assertEqual(calc_tree.get_value(), 2)

    def test_14(self):
        calcul = "1 / 0"
        calcmap = mapper.Mapper()

        print("CALCUL : ", calcul)

        calc_tree = calcmap.scan(calcul)

        try:
            calc_tree.get_value()
            self.fail("Un erreur de division par 0 est attendue")
        except decimal.DivisionByZero:
            pass

    def test_Complex(self):
        calcul = "(9^(1/2)+3)*5.4"
        calcmap = mapper.Mapper()

        print("CALCUL : ", calcul)

        calc_tree = calcmap.scan(calcul)

        self.assertAlmostEqual(calc_tree.get_value(), decimal.Decimal(32.4))

    def test_sqrt(self):
        calcul = "sqrt(4)"
        calcmap = mapper.Mapper()

        print("CALCUL : ", calcul)

        calc_tree = calcmap.scan(calcul)

        self.assertAlmostEqual(calc_tree.get_value(), 32.4)


if __name__ == '__main__':
    unittest.main()
