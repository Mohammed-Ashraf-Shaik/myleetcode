# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        s = dummy
        f = dummy
        for i in range(n + 1):
            f = f.next
        while f:
            s=s.next
            f=f.next
        s.next=s.next.next
        return dummy.next