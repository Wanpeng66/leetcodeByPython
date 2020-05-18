# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 22:07
# @Author  : wanpeng
# 69. x 的平方根

class P69(object):

    def mySqrt(self, x: int) -> int:
        start, end, res = 0, x, -1
        while start <= end:
            middle = start + ((end - start) >> 1)
            if middle * middle <= x:
                start = middle + 1
                res = middle
            else:
                end = middle - 1
        return res

