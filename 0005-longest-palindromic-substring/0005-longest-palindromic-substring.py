class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        st=0
        e=0
        def ispali(s,left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return right-left-1 
        for i in range(len(s)):
            len1=ispali(s,i,i)
            len2=ispali(s,i,i+1)
            lenn=max(len1,len2)
            if lenn>(e-st):
                st=i-(lenn-1)//2
                e=i+lenn//2
        return s[st:e+1]
        