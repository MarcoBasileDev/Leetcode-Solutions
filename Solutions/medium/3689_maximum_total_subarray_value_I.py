class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        minValue = min(nums)
        maxValue = max(nums)

        return (maxValue - minValue) * k
    
        # Time complexity: O(n)
        # Space complexity: O(1)