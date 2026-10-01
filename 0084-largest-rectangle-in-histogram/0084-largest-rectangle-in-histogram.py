class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        ma=0
        st=[]
        for i in range(len(heights)+1):
            h= 0 if i==len(heights) else heights[i]
            while st and h<heights[st[-1]]:
                height=heights[st.pop()]
                width= i if not st else i-st[-1]-1
                area=height*width
                ma=max(ma,area)
            st.append(i)
        return ma