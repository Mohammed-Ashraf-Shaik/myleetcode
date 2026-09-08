class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n>999:
            ans=n-1000+1
            return ans
        else:
            return 0
        