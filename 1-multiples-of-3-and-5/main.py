#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve():
    return sum([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0])


print(solve())
