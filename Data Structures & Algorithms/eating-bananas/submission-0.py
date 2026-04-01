class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r
        while l <= r:
            k = 0
            m = (r + l) // 2
            for pile in piles:
                if pile % m != 0:
                    k += pile // m + 1
                else:
                    k += pile // m
            if k <= h:
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans 

