class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        s=[]
        for i in range(len(asteroids)):
            while s and s[-1]>0 and asteroids[i]<0 and s[-1]<abs(asteroids[i]):
                s.pop()
            if s and asteroids[i]<0 and s[-1]>0:
                if s[-1]==abs(asteroids[i]):
                    s.pop()
            else:
                s.append(asteroids[i])
        return s
                
