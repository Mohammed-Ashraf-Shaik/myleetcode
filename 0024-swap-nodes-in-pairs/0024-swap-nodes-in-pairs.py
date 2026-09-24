# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        d=ListNode(0,head)
        p=d
        while p.next and p.next.next:
            s1=p.next
            s2=s1.next
            s1.next=s2.next
            s2.next=s1
            p.next=s2
            p=s1
        return d.next