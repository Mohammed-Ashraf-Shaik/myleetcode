# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        if head==None:
            return None
        d=ListNode(0,head)
        c=d
        while c:
            if c.next and c.next.val==val:
              while c.next and c.next.val==val:
                c.next=c.next.next
              c=c.next
            else:
                c=c.next
        return d.next
