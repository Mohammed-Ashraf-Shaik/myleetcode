class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l=0
        h=len(arr)-k
        while l<h:
            m=(l+h)//2
            if abs(arr[m]-x)<=abs(arr[m+k]-x):
                h=m
            else:
                l=m+1
        return arr[l:l+k]