class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        def atmost(k):
            if k<0:
                return 0
            l=0
            s=0
            c=0
            for r in range(len(nums)):
                s+=nums[r]
                while s>k:
                    s-=nums[l]
                    l+=1
                c+=r-l+1
            return c
        return atmost(goal)-atmost(goal-1)