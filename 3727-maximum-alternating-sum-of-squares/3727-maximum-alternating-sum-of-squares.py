class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            nums[i]=nums[i]**2
        nums.sort()
        a=len(nums)
        for i in range(a//2):
            ans+=nums[a-1-i]-nums[i]
        if a%2==1:
            ans+=nums[a//2]
        return ans