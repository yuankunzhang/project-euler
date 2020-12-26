#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def solve(n):
    if n % 2 == 0:
        return solve(n / 2)

    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return solve(n / i)

    return n


print(solve(600851475143))
