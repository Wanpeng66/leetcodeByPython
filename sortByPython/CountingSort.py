# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 21:12
# @Author  : wanpeng
# 计数排序的python实现
import sys
from typing import List


class CountingSort(object):

    def cs(self, nums: List[int]) -> List[int]:
        maxVal = -sys.maxsize
        l = len(nums)
        for i in range(l):
            if nums[i] > maxVal:
                maxVal = nums[i]

        maxVal += 1
        tmp: List[int] = []
        for i in range(maxVal):
            tmp.append(0)

        for i in range(l):
            tmp[nums[i]] += 1

        for i in range(1, maxVal):
            tmp[i] += tmp[i-1]

        res: List[int] = []
        for i in range(l):
            res.append(0)
        index = l - 1

        while True:
            try:
                val = nums.pop()
                res[tmp[val]-1] = val
                tmp[val] -= 1
                index -= 1
            except IndexError:
                break
        return res


if __name__ == '__main__':
    p = CountingSort()
    print(p.cs([2, 7, 1, 10, 4]))





