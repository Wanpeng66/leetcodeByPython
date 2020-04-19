# 392. 判断子序列


class P392(object):

    def recursionFind(self, s, t, index, start):
        if index >= len(s):
            return True
        if start >= len(t):
            return False

        c = s[index]
        tmp = start
        result = []
        while tmp != -1:
            if True in result:
                return True
            tmp = t.find(c, tmp)
            if tmp != -1:
                tmp += 1
                result.append(self.recursionFind(s, t, index + 1, tmp))

        if True in result:
            return True
        else:
            return False

    def isSubsequence(self, s: str, t: str) -> bool:
        if not str:
            return True
        index = 0
        start = 0
        if t.find(s) != -1:
            return True
        return self.recursionFind(s, t, index, start)


if __name__ == '__main__':
    p = P392()
    print(p.isSubsequence("abc", "ahbgdc"))
