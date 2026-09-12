class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c_ones_c=0
        m_ones_c=0
        i=0
        while i<len(nums):
            if nums[i]==1:
                c_ones_c+=1
            else:
                m_ones_c=max(m_ones_c,c_ones_c)
                c_ones_c=0
            i+=1
        return max(m_ones_c,c_ones_c)