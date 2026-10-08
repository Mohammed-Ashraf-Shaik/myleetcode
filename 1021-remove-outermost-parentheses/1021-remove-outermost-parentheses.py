class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        co=0
        cc=0
        ans=""
        for i in s:
            if i=="(":
                co+=1
                if co>1:
                    ans+=i
            else:
                cc+=1
                if co!=cc:
                    ans+=i
                if cc==co:
                    co=0
                    cc=0
        return ans     