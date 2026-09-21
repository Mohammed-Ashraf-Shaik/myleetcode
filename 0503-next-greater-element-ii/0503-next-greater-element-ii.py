class Solution(object):
    def nextGreaterElements(self, nums):
        n=len(nums)
        ans=[-1]*n
        s=[]

        for i in range(2*n-1,-1,-1):
            x=nums[i%n]

            while s and s[-1] <= x:
                s.pop()

            if i < n and s:
                ans[i]=s[-1]

            s.append(x)

        return ans