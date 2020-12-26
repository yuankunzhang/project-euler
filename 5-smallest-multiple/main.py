#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve():
    answer = 1
    nums = [i for i in range(2, 21)]

    while True:
        if not nums:
            break

        cur = nums[0]
        answer *= cur
        nums = [i / cur if i % cur == 0 else i for i in nums[1:]]

    return answer


print(solve())
