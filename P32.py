class P32(object):

    def longestValidParentheses(self, s: str) -> int:
        arr: list = list(s)
        stack: list[int] = []
        maxVal = 0
        stack.append(-1)
        for i in range(len(arr)):
            if arr[i] == "(":
                stack.append(i)
            else:
                if len(stack) > 0:
                    stack.pop()
                if len(stack) > 0:
                    maxVal = max(maxVal, i - stack[-1])
                else:
                    stack.append(i)
        return maxVal



if __name__ == '__main__':
    p = P32()
    print(p.longestValidParentheses("()(())"))
