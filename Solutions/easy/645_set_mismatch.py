class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0, 0]

        for num in nums:
            num = abs(num)
            nums[num - 1] *= -1

            if nums[num - 1] > 0:
                res[0] = num

        for i, num in enumerate(nums):
            if num > 0 and i + 1 != res[0]:
                res[1] = i + 1
                return res


    # Time Complexity O(n)
    # Space Complexity O(1)