class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        n=len(nums)
        windowsum=0
        maxsum=0
        f={}
        for i in range(k):
            windowsum+=nums[i]
            if nums[i] not in f:
                f[nums[i]]=1
            else:
                f[nums[i]]+=1
            if len(f)==k:
                maxsum=windowsum
        for i in range(k,n):
            removefe=nums[i-k]

            
            f[removefe]-=1
            
            if f[removefe]==0:
                del f[removefe]
            
            windowsum+=nums[i]
            windowsum-=nums[i-k]
            
            if nums[i] not in f:
                f[nums[i]]=1
            else:
                f[nums[i]]+=1
           
            
            if len(f)==k:
                maxsum=max(maxsum,windowsum)
        return maxsum