#!/usr/bin/env python3
"""Peter Rasmussen, Programming Assignment 1, utils.py

This module provides miscellaneous utility functions for this package.

"""


def compute_factorial(n: int) -> int:
    """
    Compute n-factorial.
    :param n: Number to compute factorial for
    :return: n-factorial
    """
    if (not isinstance(n, int)) or (n < 0):
        raise ValueError("compute_factorial() only accepts non-negative integer values.")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


def n_choose_k(n, m=2) -> int:
    """
    Return number of ways to draw a subset of size m from set of size n.
    :param n: Set size
    :param m: Size of each subset
    :return: Number of ways to draw a subset of size m from set of size n
    """
    integers = (not isinstance(n, int)) or (not isinstance(m, int))
    nonnegative = (n >= 0) and (m >= 0)
    if integers and nonnegative:
        raise TypeError("The parameters n and m must be non-negative integers.")
    if m > n:
        raise ValueError("The parameter m must be less than or equal to n.")
    return int(compute_factorial(n) / (compute_factorial(m) * compute_factorial(n - m)))
