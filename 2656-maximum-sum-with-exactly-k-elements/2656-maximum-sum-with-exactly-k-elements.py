class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        ans=0
        l=nums[-1]
        for i in range(k):
            ans+=l+i
        return ans
        