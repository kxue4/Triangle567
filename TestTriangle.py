# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author: kx
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(-3, -4, -5), 'InvalidInput', '-3,-4,-5 should be invalid input')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(200, 300, 400), 'InvalidInput', '200,300,400 should be invalid input')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(1.2, 1.3, 1.4), 'InvalidInput', '1.2,1.3,1.4 should be invalid input')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 is not a triangle')

    def testNotATriangleB(self):
        self.assertNotEqual(classifyTriangle(6, 7, 8), 'NotATriangle', '6,7,8 is a valid triangle')

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertNotEqual(classifyTriangle(5, 4, 4), 'Right', '5,4,4 is not a Right triangle')
        
    def testEquilateralTriangleA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testEquilateralTriangleB(self):
        self.assertNotEqual(classifyTriangle(1, 2, 2), 'Equilateral', '1,2,2 should not be equilateral')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 2), 'Isosceles', '1,2,2 should be isosceles')

    def testIsoscelesTriangleB(self):
        self.assertNotEqual(classifyTriangle(1, 2, 3), 'Isosceles', '1,2,3 should not be isosceles')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene', '1,2,3 should be scalene')

    def testScaleneTriangleB(self):
        self.assertNotEqual(classifyTriangle(3, 4, 4), 'Scalene', '3,4,4 should not be scalene but isosceles')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

