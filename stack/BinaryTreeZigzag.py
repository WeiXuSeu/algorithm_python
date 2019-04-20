# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        stack1 = []
        stack2 = []
        if root is None:
            return result
        stack1.append(root)
        i = 0
        while stack1:
            list_item = [x.val for x in stack1]
            result.append(list_item)
            if i % 2 == 0:
                for index in range(len(stack1)-1, -1, -1):
                    if stack1[index].right:
                        stack2.append(stack1[index].right)
                    if stack1[index].left:
                        stack2.append(stack1[index].left)
            else:
                for index in range(len(stack1)-1, -1, -1):
                    if stack1[index].left:
                        stack2.append(stack1[index].left)
                    if stack1[index].right:
                        stack2.append(stack1[index].right)
            stack1 = stack2
            stack2 = []
            i += 1
        return result


if __name__ == "__main__":
    root = TreeNode(3)
    left1 = TreeNode(9)
    right1 = TreeNode(20)
    root.left = left1
    root.right = right1
    right1.left = TreeNode(15)
    right1.right = TreeNode(7)

    solution = Solution()
    print solution.zigzagLevelOrder(root)
    pass