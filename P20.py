class P20(object):

    def isValid(self, s: str) -> bool:
        arr: list = list(s)
        stack = []
        length = len(arr)
        for i in range(length):
            char: str = arr[i]
            if char == ")":
                try:
                    tmp = stack.pop()
                    if tmp != "(":
                        return False
                except IndexError:
                    return False

            elif char == "}":
                try:
                    tmp = stack.pop()
                    if tmp != "{":
                        return False
                except IndexError:
                    return False
            elif char == "]":
                try:
                    tmp = stack.pop()
                    if tmp != "[":
                        return False
                except IndexError:
                    return False
            else:
                stack.append(char)
        if len(stack) != 0:
            return False
        return True


if __name__ == '__main__':
    p = P20()
    print(p.isValid("{[]}"))
