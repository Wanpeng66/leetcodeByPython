# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 19:46
# @Author  : wanpeng
# 归并排序的python实现
from typing import List


class RecursionSort(object):

    def recursionSort(self, nums: List[int]) -> List[int]:
        return self.rs(nums, 0, len(nums)-1)

    def rs(self, nums: List[int], start, end) -> List[int]:
        if start >= end:
            return [nums[start]]
        middle = (start + end) >> 1
        l1 = self.rs(nums, start, middle)
        l2 = self.rs(nums, middle + 1, end)
        tmp: List[int] = []
        return self.merge(tmp, l1, l2)

    def merge(self, tmp, l1, l2) -> List[int]:
        s1, s2 = len(l1), len(l2)
        i1, i2 = 0, 0
        while i1 < s1 and i2 < s2:
            if l1[i1] <= l2[i2]:
                tmp.append(l1[i1])
                i1 += 1
            else:
                tmp.append(l2[i2])
                i2 += 1
        while i1 < s1:
            tmp.append(l1[i1])
            i1 += 1
        while i2 < s2:
            tmp.append(l2[i2])
            i2 += 1
        return tmp


if __name__ == '__main__':
    p = RecursionSort()
    print(p.recursionSort([2, 7, 1, 10, 4]))