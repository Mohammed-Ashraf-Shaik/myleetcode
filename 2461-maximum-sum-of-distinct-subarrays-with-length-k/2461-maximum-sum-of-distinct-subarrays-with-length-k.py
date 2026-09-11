class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d={}
        c_sum=0
        m_sum=0
        l=0
        r=k
        for i in range(k):
            d[nums[i]]=d.get(nums[i],0)+1
            c_sum+=nums[i]
            if len(d)==k:
              m_sum=max(c_sum,m_sum)
        for j in range(k,len(nums)):
            d[nums[l]]-=1
            if d[nums[l]]==0:
                del d[nums[l]]
            d[nums[r]]=d.get(nums[r],0)+1
            c_sum=c_sum-nums[l]+nums[r]
            if len(d)==k:
              m_sum=max(c_sum,m_sum)
            l+=1
            r+=1
        return m_sum