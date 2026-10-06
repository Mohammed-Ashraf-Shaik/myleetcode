class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        o=0
        c=0
        ans=0
        for i in s:
            if i=="(":
                ans+=1
                o+=1
            else:
                if o>0:
                    ans-=1
                    o-=1
                else:
                    ans+=1
        return ans