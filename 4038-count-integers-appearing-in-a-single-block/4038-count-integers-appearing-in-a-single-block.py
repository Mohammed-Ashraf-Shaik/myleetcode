class Solution(object):
    def countSpecialIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in range(len(nums)):
            x = nums[i]
            if i == 0 or nums[i - 1] != x:
                d[x] = d.get(x, 0) + 1
    
        return sum(v == 1 for v in d.values())