class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atmost(nums,k):
            l=0
            ans=0
            c=0
            d={}
            for r in range(len(nums)):
                d[nums[r]]=d.get(nums[r],0)+1
                while len(d)>k:
                    d[nums[l]]-=1
                    if d[nums[l]]==0:
                        del d[nums[l]]
                    l+=1
                c+=r-l+1
            return c
        return atmost(nums,k)-atmost(nums,k-1)