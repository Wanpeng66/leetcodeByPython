# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 20:30
# @Author  : wanpeng
# 只出现一次的数字
from typing import List


class P136(object):

    def singleNumber(self, nums: List[int]) -> int:
        only = list(set(nums))
        for i in range(len(only)):
            val = only[i]
            if nums.count(val) == 1:
                return val
