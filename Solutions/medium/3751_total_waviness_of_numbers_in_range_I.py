class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness = 0
        
        for num in range(num1, num2 + 1):

            if num < 100:
                continue
            
            s = str(num)
            l = len(s)
            
            for i in range(1, l - 1):
                if (s[i - 1] < s[i] > s[i + 1]) or (s[i - 1] > s[i] < s[i + 1]):
                    waviness += 1
        
        return waviness
    
        # Time complexity: O(n log num2)
        # Space complexity: O(log num2)