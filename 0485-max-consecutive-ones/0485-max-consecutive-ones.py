class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        window=0
        maxwindow=0
        for i in range(len(nums)):
            if nums[i]==1:
                window+=1
                maxwindow=max(window,maxwindow)
            else:
                window=0
        return maxwindow