class Solution:
    def maxArea(self, heights: List[int]) -> int:
            l, r = 0, len(heights) - 1
            ans = 0
            area = 0
            while l <= r:
                area = min(heights[l], heights[r]) * (r - l)
                ans = max(area, ans)
                if heights[l] > heights[r]:
                    r -= 1
                else:
                    l += 1
            return ans

