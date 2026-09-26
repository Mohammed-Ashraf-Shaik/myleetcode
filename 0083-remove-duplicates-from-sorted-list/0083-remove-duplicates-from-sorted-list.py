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
        a=head 
        l=0
        while a:
            a=a.next
            l+=1
        if l==0:
            return None
        d=ListNode (0,head)
        p=d.next
        c=p.next
        while c:
            if p.val==c.val:
                p.next=c.next
                c=c.next
            else:
                c=c.next
                p=p.next
        return d.next