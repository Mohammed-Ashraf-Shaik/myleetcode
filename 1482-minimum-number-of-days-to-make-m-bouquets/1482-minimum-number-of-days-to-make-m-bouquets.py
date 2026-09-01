class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        mi=min(bloomDay)
        ma=max(bloomDay)
        def possibledays(bloomDay,day,m,k):
            c=0
            noofbs=0
            for i in range(len(bloomDay)):
                if bloomDay[i]<=day:
                    c+=1
                else:
                    noofbs+=c//k
                    c=0
            noofbs+=c//k
            return noofbs>=m
        l=mi
        h=ma
        if (m*k)>len(bloomDay):
            return -1
        while l<h:
            mid=(l+h)//2
            if possibledays(bloomDay,mid,m,k):
                h=mid
            else:
                l=mid+1
        return l