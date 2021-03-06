import json

from P94 import Solution


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Util(object):

    def stringToTreeNode(self,input):
        input = input.strip()
        input = input[1:-1]
        if not input:
            return None

        inputValues = [s.strip() for s in input.split(',')]
        root = TreeNode(int(inputValues[0]))
        nodeQueue = [root]
        front = 0
        index = 1
        while index < len(inputValues):
            node = nodeQueue[front]
            front = front + 1

            item = inputValues[index]
            index = index + 1
            if item != "null":
                leftNumber = int(item)
                node.left = TreeNode(leftNumber)
                nodeQueue.append(node.left)

            if index >= len(inputValues):
                break

            item = inputValues[index]
            index = index + 1
            if item != "null":
                rightNumber = int(item)
                node.right = TreeNode(rightNumber)
                nodeQueue.append(node.right)
        return root

    def integerListToString(self,nums, len_of_list=None):
        if not len_of_list:
            len_of_list = len(nums)
        return json.dumps(nums[:len_of_list])

