class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r=len(height)-1
        lm=height[l]
        rm=height[r]
        ans=0
        while l<r:
            if height[l]<height[r]:
                lm=max(lm,height[l])
                ans+=lm-height[l]
                l+=1
            else:
                rm=max(rm,height[r])
                ans+=rm-height[r]
                r-=1
        return ans