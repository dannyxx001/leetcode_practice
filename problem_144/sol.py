# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        current = root
        not_visit = []
        preorder_list = []
        while current:
            preorder_list.append(current.val)
            if current.right:
                not_visit.append(current.right)
            if current.left:
                current = current.left
            elif not_visit:
                current = not_visit.pop()
            else:
                break
        return preorder_list
