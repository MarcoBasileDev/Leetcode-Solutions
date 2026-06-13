class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        
        for word in words:
            s = 0

            for c in word:
                s += weights[ord(c) - ord('a')]
            
            res.append(chr(ord('z') - s % 26))

        return "".join(res)

        # Time complexity: O(n)
        # Space complexity: O(1)