class Solution:
    def checkValidString(self, s: str) -> bool:
        minn=0
        maxx=0
        for i in range(len(s)):
            if s[i]=="(":
                minn+=1
                maxx+=1
            elif s[i]==")":
                minn-=1
                maxx-=1
            else:
                minn-=1
                maxx+=1
            if maxx<0:
                return False
            if minn<0:
                minn=0
        return minn==0