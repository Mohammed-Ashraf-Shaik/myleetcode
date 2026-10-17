class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digitSum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s

        arr = []

        for x in nums:
            arr.append((digitSum(x), x))

        arr.sort()

        target = []
        for x in arr:
            target.append(x[1])

        pos = {}
        for i in range(len(nums)):
            pos[nums[i]] = i

        ans = 0

        for i in range(len(nums)):
            if nums[i] != target[i]:
                j = pos[target[i]]

                pos[nums[i]] = j
                pos[target[i]] = i

                nums[i], nums[j] = nums[j], nums[i]
                ans += 1

        return ans