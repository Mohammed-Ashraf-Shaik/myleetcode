class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        s=[]
        ans=[0]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            while s and temperatures[s[-1]]<=temperatures[i]:
                s.pop()
            if s:
                ans[i]=s[-1]-i
            s.append(i)
        return ans