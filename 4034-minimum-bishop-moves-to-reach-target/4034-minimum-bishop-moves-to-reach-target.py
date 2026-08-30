class Solution(object):
    def minBishopMoves(self, source, target):
        """
        :type source: List[int]
        :type target: List[int]
        :rtype: int
        """
        sr=source[0]
        sc=source[1]
        tr=target[0]
        tc=target[1]
        if source==target:
            return 0
        elif abs(sr-tr)==abs(sc-tc):
            return 1
        elif (sr+sc)%2==(tr+tc)%2:
            return 2
        else:
            return -1