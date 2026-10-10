class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)

        diff = []
        for i in range(n):
            diff.append(abs(nums1[i] - nums2[i]))

        maxDiff = max(diff)

        countDiff = [0] * (maxDiff + 1)
        for d in diff:
            countDiff[d] += 1

        K = k1 + k2

        for currDiff in range(maxDiff, 0, -1):
            if K <= 0:
                break

            countOps = min(countDiff[currDiff], K)

            countDiff[currDiff] -= countOps
            countDiff[currDiff - 1] += countOps
            K -= countOps

        result = 0
        for d in range(1, maxDiff + 1):
            result += countDiff[d] * d * d

        return result