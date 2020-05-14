# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 21:02
# @Author  : wanpeng
# 冒泡排序的python实现
from typing import List


class BubbleSort(object):

    def bs(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for i in range(size):
            flag = False
            for j in range(size - i - 1):
                if nums[j] > nums[j + 1]:
                    flag = True
                    tmp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = tmp
            if not flag:
                break
        return nums


if __name__ == '__main__':
    p = BubbleSort()
    print(p.bs([2, 7, 1, 10, 4]))
