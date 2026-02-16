#!/usr/bin/python3
"""Defines the pascal_triangle function."""


def pascal_triangle(n):
    """Returns the Pascal triangle of n.

    Parameters:
        n: The number to use as base.

    Returns: Array representing the Pascal triangle of n."""

    if n <= 0:
        return []
    t = [[1]]
    for i in range(1, n):
        r = [1]
        for j in range(1, i):
            r.append(t[i - 1][j - 1] + triangle[i - 1][j])
        r.append(1)
        t.append(r)
    return t
