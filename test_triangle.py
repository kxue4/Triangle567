#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2/13/18 13:52
# @Author  : Kaiwen Xue
# @File    : test_triangle.py
# @Software: PyCharm
"""
A unit test script to test triangle_kxue
"""
import unittest
from triangle import classify_triangle


class TestTriangles(unittest.TestCase):
    """
    test cases to test classify_triangle function
    """
    def test_invalid_input_a(self):
        """
        test invalid input >200
        """
        self.assertEqual(classify_triangle(400, 400, 400), 'not valid')

    def test_invalid_input_b(self):
        """
        negative test invalid input
        """
        self.assertNotEqual(classify_triangle(4, 5, 6), 'not valid')

    def test_invalid_input_c(self):
        """
        test invalid input <0
        """
        self.assertEqual(classify_triangle(-3, -4, -5), 'not valid')

    def test_invalid_input_d(self):
        """
        test invalid input not number
        """
        self.assertEqual(classify_triangle('a', 'b', 'c'), 'not valid')

    def test_not_a_triangle_a(self):
        """
        negative test not a triangle
        """
        self.assertNotEqual(classify_triangle(6, 7, 8), 'not valid')

    def test_not_a_triangle_b(self):
        """
        test not a triangle
        """
        self.assertEqual(classify_triangle(1, 2, 3), 'not valid')

    def test_right_triangle_a(self):
        """
        test right triangle
        """
        self.assertEqual(classify_triangle(3, 4, 5), 'Right scalene')

    def test_right_triangle_b(self):
        """
        test right triangle with numerical precision
        """
        self.assertEqual(classify_triangle(3, 4, 5.0001), 'Right scalene')

    def test_equilateral_triangle_a(self):
        """
        test equilateral triangle
        """
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral')

    def test_isosceles_triangle_a(self):
        """
        test isosceles triangle
        """
        self.assertEqual(classify_triangle(1, 2, 2), 'Isosceles')

    def test_right_isosceles_triangle_a(self):
        """
        test right isosceles triangle with numerical precision
        """
        self.assertEqual(classify_triangle(1, 1, 1.414), 'Right isosceles')

    def test_right_scalene_triangle_a(self):
        """
        test right scalene triangle
        """
        self.assertEqual(classify_triangle(3, 4, 5), 'Right scalene')

    def test_scalene_triangle_a(self):
        """
        test scalene triangle
        """
        self.assertEqual(classify_triangle(4, 5, 6), 'Scalene')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
