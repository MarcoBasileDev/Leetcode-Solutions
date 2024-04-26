class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26

        for i in range(len(s)):
            n = ord(s[i]) - ord('a')
            mx = 1

            for j in range(26):
                if abs(j - n) <= k:
                    mx = max(mx, dp[j] + 1)

            dp[n] = mx
        
        res = 0

        for x in dp:
            res = max(res, x)
            
        return res

        # Time Complexity O(n)
        # Space Complexity O(1)