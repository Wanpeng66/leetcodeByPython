# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 21:21
# @Author  : wanpeng
# 插入排序的python实现
from typing import List


class InsertionSort(object):

    def Is(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for i in range(1, size):
            j = i
            tmp = nums[j]
            while j > 0:
                if tmp < nums[j-1]:
                    nums[j] = nums[j-1]
                    j -= 1
                else:
                    break
            nums[j] = tmp
        return nums


if __name__ == '__main__':
    p = InsertionSort()
    print(p.Is([2, 7, 1, 10, 4]))