from Queue import Queue
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root:
            q = Queue()
            q.put(root)
            all = []
            while not q.empty():
                current = q.get()
                if current.left:
                    current.left.val += current.val
                    q.put(current.left)
                if current.right:
                    current.right.val += current.val
                    q.put(current.right)
                if not current.left and not current.right:
                    all.append(current.val)
            if sum in all:
                return True
        return False