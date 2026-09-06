class Solution(object):
    def findAnagrams(self, s, p):
        n = len(s)
        k = len(p)

        if k > n:
            return []

        kpc = [0] * 26
        nsc = [0] * 26
        res = []

        for ch in p:
            kpc[ord(ch) - ord('a')] += 1

        for j in range(k):
            nsc[ord(s[j]) - ord('a')] += 1

        if kpc == nsc:
            res.append(0)

        for i in range(1, n-k+1):
            nsc[ord(s[i-1]) - ord('a')] -= 1
            nsc[ord(s[i+k-1]) - ord('a')] += 1

            if kpc == nsc:
                res.append(i)

        return res