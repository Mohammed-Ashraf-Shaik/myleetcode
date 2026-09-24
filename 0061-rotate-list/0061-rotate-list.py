# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head==None or k==0 or head.next==None:
            return head
        cur=head
        l=1
        while cur.next:
            cur=cur.next
            l+=1
        steps=k%l
        if steps==0:
            return head
        cur.next=head 
        
        """ circular kara bhai edar mai"""
        
        newcurr=head   
        
        """new head liya circular list ku"""
        
        for i in range(l-steps-1):
            newcurr=newcurr.next
        newhead=newcurr.next
        newcurr.next=None
        return newhead
         