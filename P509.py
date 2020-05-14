# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 20:07
# @Author  : wanpeng
# 求斐波那契数列的第n项值


class P509(object):

    def __init__(self):
        self.res: dict = {}

    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            if self.res.get(N):
                return self.res.get(N)
            else:
                r = self.fib(N-1) + self.fib(N-2)
                self.res.setdefault(N, r)
                return r


if __name__ == '__main__':
    p = P509()
    print(p.fib(0))

