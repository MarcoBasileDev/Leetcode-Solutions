class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = [0] * 101
        res = [0] * len(nums)

        for num in nums:
            freq[num] += 1

        for num in range(1, 101):
            freq[num] += freq[num - 1]

        for i in range(len(nums)):
            v = nums[i]

            if v == 0:
                res[i] = 0
            else:
                res[i] = freq[v - 1]

        return res

    # Time Complexity O(n + K)
    # Space Complexity O(n)