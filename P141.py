class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class P141(object):

    def hasCycle(self, head: ListNode) -> bool:
        nodes = set([])
        while head:
            if head not in nodes:
                nodes.add(head)
                head = head.next
            else:
                return True
        return False
