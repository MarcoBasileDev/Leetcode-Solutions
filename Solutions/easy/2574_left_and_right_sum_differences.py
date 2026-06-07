class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        leftSum = 0
        for i in range(n):
            res[i] = leftSum
            leftSum += nums[i]

        rightSum = 0
        for i in range(n - 1, -1, -1):
            res[i] = abs(res[i] - rightSum)
            rightSum += nums[i]

        return res
    
        # Time complexity: O(n)
        # Space complexity: O(1)