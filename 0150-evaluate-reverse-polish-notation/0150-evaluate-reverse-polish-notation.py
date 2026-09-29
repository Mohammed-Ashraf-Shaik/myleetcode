class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        s=[]
        for i in tokens:
            if i in "+-*/":
                b=s.pop()
                a=s.pop()
                if i=="+":
                    s.append(a+b)
                elif i=='-':
                    s.append(a-b)
                elif i=="*":
                    s.append(a*b)
                else:
                    s.append(int(float((a)/b)))
            else:
                s.append(int(i))
        return s[-1]    