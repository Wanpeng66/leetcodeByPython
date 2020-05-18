# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 20:39
# @Author  : wanpeng
# 4. 寻找两个正序数组的中位数
from typing import List


class P4(object):

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s1, s2 = len(nums1), len(nums2)
        doubleFlag = (s1 + s2) % 2 == 0
        res = []
        i1, i2 = 0, 0
        while i1 < len(nums1) or i2 < len(nums2):
            if i1 < len(nums1) and i2 < len(nums2) and nums1[i1] <= nums2[i2]:
                res.append(nums1[i1])
                i1 += 1
            elif i1 < len(nums1) and i2 < len(nums2) and nums1[i1] > nums2[i2]:
                res.append(nums2[i2])
                i2 += 1
            elif i1 < len(nums1) and i2 >= len(nums2):
                res.append(nums1[i1])
                i1 += 1
            elif i2 < len(nums2) and i1 >= len(nums1):
                res.append(nums2[i2])
                i2 += 1

            if len(res) - 1 == (s1 + s2) >> 1:
                break

        if doubleFlag:
            return (res[-2] + res[-1]) / 2
        else:
            return res[-1]


if __name__ == '__main__':
    p = P4()
    print(p.findMedianSortedArrays([1, 2], [3, 4]))
