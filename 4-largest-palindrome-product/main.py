#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def solve():
    palindromes = []

    for i, j in [(i, j) for i in range(999, 99, -1) for j in range(999, 99, -1)]:
        if is_palindrome(i * j):
            palindromes.append(i * j)

    return max(palindromes)

print(solve())
