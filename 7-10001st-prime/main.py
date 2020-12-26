#!/usr/bin/env python
# -*- coding: utf-8 -*-


def prime():
    primes = []
    while True:
        if not primes:
            primes.append(2)
            yield 2
            continue
        n = primes[-1] + 1
        while True:
            if all([n % i != 0 for i in primes]):
                break
            n += 1
        primes.append(n)
        yield n


def solve(n):
    for i in prime():
        print(i)
        if n == 1:
            return i
        n -= 1


print(solve(10001))
