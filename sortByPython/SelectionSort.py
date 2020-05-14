# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 21:53
# @Author  : wanpeng
# 选择排序的python实现
import sys
from typing import List


class SelectionSort(object):

    def ss(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for i in range(size):
            minVal = sys.maxsize
            index = i
            for j in range(i, size):
                if nums[j] < minVal:
                    minVal = nums[j]
                    index = j
            tmp = nums[index]
            nums[index] = nums[i]
            nums[i] = tmp
        return nums


if __name__ == '__main__':
    p = SelectionSort()
    print(p.ss([2, 7, 1, 10, 4]))