# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import OrderedDict
        result = OrderedDict()
        stack = []
        if root is None:
            return []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            if stack and not stack[-1].right:
                result[stack[-1]] = stack[-1].val
                stack.pop()
            if stack:
                curr = stack[-1]
            while curr and (not curr.right or curr.right in result):
                result[curr] = curr.val
                stack.pop()
                curr = stack[-1] if stack else None
            curr = stack[-1].right if stack else None
        return result.values()


if __name__ == "__main__":
    x = TreeNode(1)
    y = TreeNode(2)
    z = TreeNode(3)
    x.right = y
    y.left = z
    solution = Solution()
    print solution.postorderTraversal(x)
