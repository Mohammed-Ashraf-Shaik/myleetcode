class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        result=float("inf")
        for start in range(len(nums)):
            csum=0
            for end in range(start,len(nums)):
                csum+=nums[end]
                length=end-start+1
                if l<=length<=r:
                    if csum>0:
                        result=min(result,csum)
        return -1 if result==float("inf") else result