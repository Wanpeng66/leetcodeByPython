# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 21:16
# @Author  : wanpeng
# 18. 四数之和
from typing import List


class P18(object):

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res: List[List[int]] = []
        size = len(nums)
        nums.sort()
        for x in range(size - 3):
            for y in range(x + 1, size - 2):
                start, end = y + 1, size - 1
                while start < end:
                    if nums[x] + nums[y] + nums[start] + nums[end] > target:
                        end -= 1
                    elif nums[x] + nums[y] + nums[start] + nums[end] < target:
                        start += 1
                    else:
                        solve = [nums[x], nums[y], nums[start], nums[end]]
                        if solve not in res:
                            res.append(solve)
                        start += 1

        return res

    def method1(self, nums, target):
        res: List[List[int]] = []
        size = len(nums)
        nums.sort()
        for x in range(size - 3):
            for y in range(x + 1, size - 2):
                for z in range(y + 1, size - 1):
                    for i in range(z + 1, size):
                        if nums[x] + nums[y] + nums[z] + nums[i] == target:
                            solve = [nums[x], nums[y], nums[z], nums[i]]
                            if solve not in res:
                                res.append(solve)
        return res


if __name__ == '__main__':
    p = P18()
    print(p.fourSum([-3, -1, 0, 2, 4, 5], 0))
