class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        l=[]
        def solve(n,o,c,t):
            if o==0 and c==0:
                l.append(t)
                return 
            if o>=1:
                solve(n,o-1,c+1,t+'(')
            if c>=1:
                solve(n,o,c-1,t+')')
            return 
        solve(n,n,0,"")
        return l