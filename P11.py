# 11. 盛最多水的容器
from typing import List


class P11(object):

    def maxArea(self, height: List[int]) -> int:
        begin = 0
        end = len(height)-1
        max = 0
        while begin < end:
            left = height[begin]
            right = height[end]
            tmp = (end-begin)*min(left, right)
            if tmp > max:
                max = tmp
            if left > right:
                end -= 1
            else:
                begin += 1
        return max

    def method1(self, height):
        max = 0
        cache = {}
        length = len(height)
        for i in range(length):
            for k in range(i, length):
                width = k - i
                h = min(height[i], height[k])
                tmp = cache.get(str(width) + "," + str(h))
                if not tmp:
                    tmp = width * h
                    cache[str(width) + "," + str(h)] = tmp
                if tmp > max:
                    max = tmp
        return max
