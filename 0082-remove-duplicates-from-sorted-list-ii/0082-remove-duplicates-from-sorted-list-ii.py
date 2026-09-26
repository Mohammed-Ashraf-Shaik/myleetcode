# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head==None:
            return None
        d=ListNode(0,head)
        p=d
        c=p.next
        while c:
            if c.next and c.val==c.next.val:
                while c.next and c.val==c.next.val:
                    c=c.next
                c=c.next
                p.next=c
            else:
                c=c.next
                p=p.next
        return d.next
