class Solution:
    def increasingTriplet(self, nums):
        first = second = float('inf')
        
        for n in nums:
            # If n is less than f, n can be a potential candidate as first element
            if n <= first:
                first = n
            # f < n < s
            elif n <= second:
                second = n
            # n is greater than both f and s
            else:
                return True
        
        return False

        # Time Complexity O(n)
        # Space Complexity O(1)