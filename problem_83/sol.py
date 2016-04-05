# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            current = head.next
            prev = head
            tmp = head.val
            while current != None:
                if current.val != tmp:
                    tmp = current.val
                    prev.next = current
                    prev = current
                current = current.next
            prev.next = current
        return head
