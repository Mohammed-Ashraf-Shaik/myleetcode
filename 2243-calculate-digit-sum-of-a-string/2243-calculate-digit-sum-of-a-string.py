class Solution:
    def digitSum(self, s: str, k: int) -> str:
        news=[]
        while len(s)>k:
            for i in range(0,len(s),k):
                group=s[i:i+k]
                summ=0
                for ch in group:
                    summ+=int(ch)
                news.append(str(summ))
            s="".join(news)
            news=[]
        return s