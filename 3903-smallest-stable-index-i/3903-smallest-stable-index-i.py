class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        curmax = float('-inf')
        for i in range(len(nums)):
            curmax = max(curmax, nums[i])
            curmin = float('inf')
            for j in range(i, len(nums)):
                curmin = min(curmin, nums[j])
            if curmax - curmin <= k:
                return i
        return -1