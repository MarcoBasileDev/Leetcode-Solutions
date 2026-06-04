class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        return nums[0] + sum(nsmallest(2, nums[1:]))
    
        # Time complexity: O(n)
        # Space complexity: O(1)