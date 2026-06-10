from typing import List

class SegTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)

        self.maxv = [0] * (2 * self.n)
        self.minv = [0] * (2 * self.n)

        for i, x in enumerate(nums):
            self.maxv[self.n + i] = x
            self.minv[self.n + i] = x

        for i in range(self.n - 1, 0, -1):
            self.maxv[i] = max(self.maxv[i * 2], self.maxv[i * 2 + 1])
            self.minv[i] = min(self.minv[i * 2], self.minv[i * 2 + 1])

    def queryMax(self, l: int, r: int) -> int:
        l += self.n
        r += self.n

        ans = -10**18

        while l <= r:
            if l & 1:
                ans = max(ans, self.maxv[l])
                l += 1

            if not (r & 1):
                ans = max(ans, self.maxv[r])
                r -= 1

            l //= 2
            r //= 2

        return ans

    def queryMin(self, l: int, r: int) -> int:
        l += self.n
        r += self.n

        ans = 10**18

        while l <= r:
            if l & 1:
                ans = min(ans, self.minv[l])
                l += 1

            if not (r & 1):
                ans = min(ans, self.minv[r])
                r -= 1

            l //= 2
            r //= 2

        return ans

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        seg = SegTree(nums)

        pq = [
            (
                -(seg.queryMax(l, n - 1) - seg.queryMin(l, n - 1)),
                l,
                n - 1,
            )
            for l in range(n)
        ]

        heapq.heapify(pq)

        ans = 0

        while k:
            negVal, l, r = heapq.heappop(pq)

            ans -= negVal
            k -= 1

            if l < r:
                heapq.heappush(
                    pq,
                    (
                        -(seg.queryMax(l, r - 1) - seg.queryMin(l, r - 1)),
                        l,
                        r - 1,
                    ),
                )

        return ans

        # Time complexity: O((n+k)log n)
        # Space complexity: O(n)