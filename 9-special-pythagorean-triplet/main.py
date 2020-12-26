#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve():
    for (a, b) in [(x, y) for x in range(1, 998) for y in range(1, 998)]:
        c = 1000 - a - b
        if a * a + b * b == c * c:
            return a * b * c, a, b, c


print(solve())
