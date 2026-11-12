class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc=1
        dec=1
        if len(nums)==1:
            return 1
        prevel=nums[0]
        result=1
        for i in range(1,len(nums)):
            if nums[i]>prevel:
                inc+=1
                dec=1
                result=max(result,inc)
            elif nums[i]<prevel:
                inc=1
                dec+=1
                result=max(result,dec)
            else:
                inc=1
                dec=1
            prevel=nums[i]
            
        return result
            