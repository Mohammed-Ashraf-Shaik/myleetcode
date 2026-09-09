class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        start=1000
        c=1
        ans=0
        while start<=n:
            end=min(n,start*1000-1)
            ans+=(end-start+1)*c
            start*=1000
            c+=1
        return ans