class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        for i in range(n - m + 1):
            j = 0

            while j < m and haystack[i + j] == needle[j]:
                j += 1

            if j == m:
                return i

        return -1
    
        # Time complexity: O(n * m)
        # Space complexity: O(1)