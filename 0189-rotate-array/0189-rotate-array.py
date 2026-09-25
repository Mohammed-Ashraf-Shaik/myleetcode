class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        k=k%l
        c=0
        i=0
        while c<l:
            j=i
            t=nums[i]
            while True:
                j=(j+k)%l
                nums[j],t=t,nums[j]
                c+=1
                if j==i:
                    break
            i+=1
        return nums

            