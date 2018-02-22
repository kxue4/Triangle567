#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2/13/18 13:52
# @Author  : Kaiwen Xue
# @File    : TestTriangle.py
# @Software: PyCharm
import unittest
from Triangle import classify_triangle


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testInvalidInputA(self):
        self.assertEqual(classify_triangle(400, 400, 400), 'not valid', '400,400,400 should be invalid input')

    def testInvalidInputB(self):
        self.assertNotEqual(classify_triangle(4, 5, 6), 'not valid', '4,5,6 should be   valid input')

    def testInvalidInputC(self):
        self.assertEqual(classify_triangle(-3, -4, -5), 'not valid', '-3,-4,-5 should be invalid input')

    def testNotATriangleA(self):
        self.assertNotEqual(classify_triangle(6, 7, 8), 'not valid', '6,7,8 is a valid triangle')

    def testNotATriangleB(self):
        self.assertEqual(classify_triangle(1, 2, 3), 'not valid', '1,2,3 is not a triangle')

    def testRightTriangleA(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right scalene', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classify_triangle(3, 4, 5.0001), 'Right scalene', '3,4,5.0001 is a Right scalene triangle')

    def testEquilateralTriangleA(self):
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classify_triangle(1, 2, 2), 'Isosceles', '1,2,2 should be isosceles')

    def testRightisoscelesTriangleA(self):
        self.assertEqual(classify_triangle(1, 1, 1.414), 'Right isosceles', '1,1,1.414 should be right isosceles')

    def testRightscaleneTriangleA(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right scalene', '3,4,5 should be scalene')

    def testScaleneTriangleA(self):
        self.assertEqual(classify_triangle(4, 5, 6), 'Scalene', '1,2,3 should be scalene')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
