class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        st=[-1]
        maxx=0
        for i in range(len(s)):
            if s[i]=="(":
                st.append(i)
            else:
                st.pop()
                
                if not st: 
                    st.append(i)
                else:
                    maxx=max(maxx,i-(st[-1]))
        return maxx