class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        l=0
        ans=0
        d={}
        for r in range(len(fruits)):
            d[fruits[r]]=d.get(fruits[r],0)+1
            while len(d)>2:
                d[fruits[l]]-=1
                if d[fruits[l]]==0:
                    del d[fruits[l]]
                l+=1
            ans=max(ans,r-l+1)
        return ans