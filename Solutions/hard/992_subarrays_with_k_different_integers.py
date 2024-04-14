class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.at_most(nums, k) - self.at_most(nums, k-1)
    
    def at_most(self, nums, k):
        dic = {}
        l = 0
        cnt = 0

        for r in range(len(nums)):
            dic[nums[r]] = dic.get(nums[r], 0) + 1

            while len(dic) > k:
                dic[nums[l]] -= 1

                if dic[nums[l]] == 0:
                    dic.pop(nums[l])

                l += 1

            cnt += r - l + 1

        return cnt

        # Time Complexity O(n)
        # Space Complexity O(n)