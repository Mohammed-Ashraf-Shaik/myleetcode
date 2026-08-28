class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l=1
        r=max(piles)
        ans=0
        while l<=r:
            hrs=0
            m=(l+r)//2
            for i in piles:
                hrs+=(i+m-1)//m
            if hrs<=h:
                r=m-1
                ans=m
            else:
                l=m+1
        return ans