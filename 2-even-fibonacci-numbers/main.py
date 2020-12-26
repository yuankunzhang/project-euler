#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fib():
    a = 1
    b = 2
    while True:
        yield a
        a, b = b, a + b


def solve():
    s = 0
    for i in fib():
        if i > 4000000:
            break
        if i % 2 == 1:
            continue
        s += i
    return s


print(solve())
