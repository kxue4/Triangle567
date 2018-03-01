#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/21/18 09:31
# @Author  : Kaiwen Xue
# @File    : triangle.py
# @Software: PyCharm
"""
This is a module to let user input three float number.
Then classify which type of triangle this three number combines.
"""


def classify_triangle(a_float, b_float, c_float):
    """
    The function to classify triangle type.
    """
    per = a_float + b_float + c_float
    m_float = max(a_float, b_float, c_float)
    n_float = min(a_float, b_float, c_float)
    i_float = per - m_float - n_float
    if n_float + i_float <= m_float or n_float <= 0 or m_float >= 200:
        return 'not valid'

    if round(m_float * m_float, 2) == round(i_float * i_float + n_float * n_float, 2):

        if a_float == b_float or b_float == c_float or a_float == c_float:
            return 'Right isosceles'

        return 'Right scalene'

    if a_float == b_float or b_float == c_float or a_float == c_float:

        if a_float == b_float == c_float:
            return 'Equilateral'

        return 'Isosceles'

    return 'Scalene'


def main():
    """
    This is the main() function
    """
    try:
        a_float = float(input('Please enter A: '))
        b_float = float(input('Please enter B: '))
        c_float = float(input('Please enter C: '))
    except ValueError:
        print('Not valid! Wrong input')
    else:
        result = classify_triangle(a_float, b_float, c_float)
        if result == 'not valid':
            print('Wrong input, this triangle is not valid!')
        else:
            print(classify_triangle(a_float, b_float, c_float), 'triangle.')


if __name__ == '__main__':
    main()
