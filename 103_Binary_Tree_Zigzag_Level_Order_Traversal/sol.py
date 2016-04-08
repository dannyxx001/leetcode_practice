# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root:
            s1 = []
            s2 = []
            s1.append(root)
            while s1 or s2:
                # from left to right
                an_order = []
                while len(s1):
                    current = s1.pop()
                    an_order.append(current.val)
                    if current.left:
                        s2.append(current.left)
                    if current.right:
                        s2.append(current.right)
                if an_order:
                    result.append(an_order)
                # from right to left
                an_order = []
                while len(s2):
                    current = s2.pop()
                    an_order.append(current.val)
                    if current.right:
                        s1.append(current.right)
                    if current.left:
                        s1.append(current.left)
                if an_order:
                    result.append(an_order)
        return result