# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Queue import Queue

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_found, q_found = 0, 0
        parent_map = {}
        bfs_queue = Queue()
        bfs_queue.put(root)
        bfs_queue.put(1)
        while not (p_found and q_found):
            current = bfs_queue.get()
            layer = bfs_queue.get()
            parent_map[layer] = current

            if current == p:
                p_found = layer
            elif current == q:
                q_found = layer

            if current.left != None:
                bfs_queue.put(current.left)
                bfs_queue.put(layer*2)
            if current.right != None:
                bfs_queue.put(current.right)
                bfs_queue.put(layer*2+1)
                
        #print p_found,q_found
        
        while p_found != q_found:
            if p_found > q_found:
                p_found //= 2
            else:
                q_found //= 2
        
        return parent_map[p_found]