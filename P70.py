# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 19:50
# @Author  : wanpeng
# 爬楼梯问题


class P70(object):

    def __init__(self):
        self.hasSolved: dict = {}

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            if self.hasSolved.get(n):
                return self.hasSolved.get(n)
            else:
                res = self.climbStairs(n - 1) + self.climbStairs(n - 2)
                self.hasSolved.setdefault(n, res)
                return res


if __name__ == '__main__':
    p = P70()
    print(p.climbStairs(2))