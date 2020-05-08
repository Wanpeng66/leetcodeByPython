# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 9:54
# @Author  : wanpeng
import sys
from typing import List


class P53_dynamic(object):
    # 非连续子序列最大值
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums) - 1
        res = [n]
        zero = [0, nums[0]]
        res[0] = zero

        for i in range(1, n):
            dic: list = res[i - 1]
            tmp = []
            for j in dic:
                tmp.append(j)
                tmp.append(j + nums[i])
            res.append(tmp)
        maxInt = -sys.maxsize - 1
        for i in res[-1]:
            if i > maxInt:
                maxInt = i
        return maxInt


if __name__ == '__main__':
    p = P53_dynamic()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(p.maxSubArray(nums))
