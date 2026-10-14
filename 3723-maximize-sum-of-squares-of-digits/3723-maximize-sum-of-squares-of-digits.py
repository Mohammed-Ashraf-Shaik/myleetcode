class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum>9*num:
            return ""
        res = []
        for i in range(num):
            digi = min(9,sum)
            res.append(str(digi))
            sum -= digi
        return "".join(res) if sum==0 else ""