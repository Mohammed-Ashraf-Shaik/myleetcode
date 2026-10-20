class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        l = 0
        r = len(nums) - 1

       
        while l <= r:
            m = (l + r) // 2

            if nums[m] >= target:
                r = m - 1
            else:
                l = m + 1

        start = l


        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] <= target:
                l = m + 1
            else:
                r = m - 1

        end = l

        res = []
        for i in range(start, end):
            res.append(i)

        return res