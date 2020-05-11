import sys
from typing import List

from P141 import ListNode


class P23(object):

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        length = len(lists)
        if length == 0:
            return None
        tmp = list(filter(lambda x: x is not None, lists))
        if len(tmp) == 0:
            return None
        lists = tmp
        node = ListNode(sys.maxsize, None)
        head = node
        while True:
            minVal = sys.maxsize
            index = 0
            for i in range(len(lists)):
                if lists[i].val < minVal:
                    minVal = lists[i].val
                    index = i
            node.val = minVal
            lists[index] = lists[index].next
            if lists[index] is None:
                lists.remove(None)
            if len(lists) == 0:
                break
            node.next = ListNode(sys.maxsize, None)
            node = node.next

        return head
