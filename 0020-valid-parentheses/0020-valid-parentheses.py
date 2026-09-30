class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i in "({[":
                st.append(i)
            else:
                if not st:
                    return False
                if (i=="]" and st.pop()!="[") or  \
                   (i==")" and st.pop()!="(") or  \
                   (i=="}" and st.pop()!="{"):
                    return False
        return len(st)==0
