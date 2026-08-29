class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        h=len(nums)-1
        nums.sort()
        closet=nums[0]
        while l<=h:
            m=(l+h)//2
            if abs(nums[m])<abs(closet) or (abs(nums[m])==abs(closet) and nums[m]>(closet)):
                closet=nums[m]
            if nums[m]==0:
                return 0
            elif nums[m]<0:
                l=m+1
            else:
                h=m-1
        return closet