# 641. 设计循环双端队列


class MyCircularDeque(object):

    def __init__(self, k: int):
        table: list[int] = []
        self.table = table
        self.size = 0
        self.maxSize = k

    def insertFront(self, value: int) -> bool:
        if self.size + 1 > self.maxSize:
            return False
        self.table.insert(0, value)
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size + 1 > self.maxSize:
            return False
        self.table.append(value)
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size <= 0:
            return False
        self.table.pop(0)
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size <= 0:
            return False
        self.table.pop(self.size-1)
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.size <= 0:
            return -1
        return self.table[0]

    def getRear(self) -> int:
        if self.size <= 0:
            return -1
        return self.table[-1]

    def isEmpty(self) -> bool:
        if self.size <= 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == self.maxSize:
            return True
        return False
