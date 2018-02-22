#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/21/18 09:31
# @Author  : Kaiwen Xue
# @File    : Triangle.py
# @Software: PyCharm
import unittest


def classify_triangle(a, b, c):
    per = a + b + c
    m = max(a, b, c)
    n = min(a, b, c)
    i = per - m - n
    if n + i <= m or n <= 0 or m >= 200:
        return 'not valid'
    elif round(m * m, 2) == round(i * i + n * n, 2):
        if a == b or b == c or a == c:
            return 'Right isosceles'
        else:
            return 'Right scalene'
    elif a == b or b == c or a == c:
        if a == b == c:
            return 'Equilateral'
        else:
            return 'Isosceles'
    else:
        return 'Scalene'


def main():
    try:
        a = float(input('Please enter A: '))
        b = float(input('Please enter B: '))
        c = float(input('Please enter C: '))
    except ValueError:
        print('Not valid! Wrong input')
    else:
        result = classify_triangle(a, b, c)
        if result == 'not valid':
            print('Wrong input, this triangle is not valid!')
        else:
            print(classify_triangle(a, b, c), 'triangle.')


if __name__ == '__main__':
    main()
