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
    if not(isinstance(a_float,(int, float)) and isinstance(b_float,(int, float)) and isinstance(c_float,(int, float))):
        return 'not valid'

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
