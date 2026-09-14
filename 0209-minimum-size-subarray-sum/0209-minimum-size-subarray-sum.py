class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l=0
        ans=float('inf')
        sums=0
        for r in range(len(nums)):
            sums+=nums[r]
            while sums>=target:
                lenn=r-l+1
                ans=min(ans,lenn)
                sums-=nums[l]
                l+=1
        if ans==float('inf'):
            return 0
        else:
            return ans