# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if left==right:
            return head
        dummy=ListNode(0,head)
        pl=dummy
        for i in range(1,left):
            pl=pl.next
        p=None
        c=pl.next
        for i in range((right-left)+1):
            n=c.next
            c.next=p
            p=c
            c=n
        ln=pl.next
        pl.next=p
        ln.next=c
        return dummy.next
