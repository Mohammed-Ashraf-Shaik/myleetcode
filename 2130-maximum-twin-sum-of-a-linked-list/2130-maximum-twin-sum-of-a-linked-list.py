# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        s=head
        f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        p=None
        while s:
            n=s.next
            s.next=p
            p=s
            s=n
        msm=0
        while p:
            sm=head.val+p.val
            msm=max(sm,msm)
            p=p.next
            head=head.next
        return msm