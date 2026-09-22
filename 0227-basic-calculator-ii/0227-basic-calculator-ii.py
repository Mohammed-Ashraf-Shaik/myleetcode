class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        st=[]
        n=0
        op='+'
        for i in range(len(s)+1):
            ch="+" if i==len(s) else s[i]
            if ch.isdigit():
                n=n*10 +int(ch)
            elif ch!=" ":
                if op=="+":
                    st.append(n)
                elif op=='-':
                    st.append(-n)
                elif op=="*":
                    st.append(st.pop()*n)
                elif op=="/":
                    st.append(int(float(st.pop())/n))
                op=ch
                n=0
        return sum(st)
