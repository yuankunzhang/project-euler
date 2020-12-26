#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(n):
    sum1 = sum([i for i in range(1, n + 1)]) ** 2
    sum2 = sum([i ** 2 for i in range(1, n + 1)])
    return sum1 - sum2


print(solve(100))
