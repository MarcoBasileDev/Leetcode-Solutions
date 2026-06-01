class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1      
            
        return l
        
        # Time complexity: O(log n)
        # Space complexity: O(1)