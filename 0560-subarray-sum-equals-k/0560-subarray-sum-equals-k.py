class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        d={0:1}
        pr=0
        for r in range(len(nums)):
            pr+=nums[r]
            t=pr-k
            if t in d:
                c+=d[t]
            d[pr]=d.get(pr,0)+1
        return c