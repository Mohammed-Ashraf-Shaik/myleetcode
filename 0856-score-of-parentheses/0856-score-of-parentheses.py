class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st=[0]
        for i in s:
            if i=="(":
                st.append(0)
            elif i==")":
                if st:
                    if st[-1]==0:
                        st.pop()
                        st.append(st.pop()+1)
                    else:
                        val=st[-1]
                        st.pop()
                        st.append(st.pop()+2*val)
        return st[-1]
