class Solution(object):
    def largestString(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        for x in nums:
            s = ""
            c = 0
            while x > 0:
                if x % 2 == 1:
                    if c == 26:
                        s = "zz" + s
                    else:
                        s = chr(ord('a') + c) + s
                x //= 2
                c += 1
            ans.append(s)
        return ans