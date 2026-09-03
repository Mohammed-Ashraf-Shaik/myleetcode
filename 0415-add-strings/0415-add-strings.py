class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i=len(num1)-1
        j=len(num2)-1
        cry=0
        a,b=0,0
        total=0
        ans=""
        while i>=0 or j>=0 or cry:
            if i>=0:
                a=ord(num1[i])-ord('0')
            else:
                a=0
            if j>=0:
                b=ord(num2[j])-ord('0')
            else:
                b=0
            total=a+b+cry
            d=total%10
            cry=total//10
            ans+=chr(d+ord('0'))
            i-=1
            j-=1
        return ans[::-1]