#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math


def is_prime(n):
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def solve(n):
    s = 2
    i = 3

    while True:
        if i > n:
            break
        if is_prime(i):
            s += i
        i += 1

    return s


print(solve(2000000))
