# 94. 二叉树的中序遍历
from typing import List

import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        White, Gray = 0, 1
        res = []
        stack = [(White, root)]
        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color == White:
                stack.append((White, node.right))
                stack.append((Gray, node))
                stack.append((White, node.left))
            else:
                res.append(node.val)
        return res


if __name__ == '__main__':
    input = "[1,null,2,3]"
    util = TreeNode.Util()
    root = util.stringToTreeNode(input)
    solution = Solution()
    res = solution.inorderTraversal(root)
    out = util.integerListToString(res)
    print(out)
