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
        l=0
        c=head
        while c:
            c=c.next
            l+=1
        p=l-n
        if p==0:
            return head.next
        c=head
        for i in range(p-1):
            c=c.next
        c.next=c.next.next
        return head