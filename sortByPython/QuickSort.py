# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 20:34
# @Author  : wanpeng
# 快排的python实现
from typing import List


class QuickSort(object):

    def quickSort(self, nums: List[int]) -> List[int]:
        self.qs(nums, 0, len(nums) - 1)
        return nums

    def qs(self, nums, start, end):
        if start >= end:
            return
        p = self.partition(nums, start, end)
        self.qs(nums, start, p - 1)
        self.qs(nums, p + 1, end)

    def partition(self, nums, start, end) -> int:
        p = nums[end]
        i = start
        for j in range(start, end):
            if nums[j] < p:
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp
                i += 1
        nums[end] = nums[i]
        nums[i] = p
        return i


if __name__ == '__main__':
    p = QuickSort()
    print(p.quickSort([2, 7, 1, 10, 4]))