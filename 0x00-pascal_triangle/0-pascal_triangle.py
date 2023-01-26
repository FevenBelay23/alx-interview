#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    answer = []
    if n > 0:
        for i in range(1, n + 1):
            list = []
            k = 1
            for j in range(1, i + 1):
                list.append(k)
                k = k * (i - j) // j
            answer.append(list)
    return answer
