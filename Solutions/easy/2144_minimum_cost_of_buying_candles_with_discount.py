class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        res = 0
        n = len(cost)

        for i in range(n):
            if i % 3 != 2:
                res += cost[i]

        return res

        # Time Complexity O(n log n)
        # Space Complexity O(log n)