class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l = 0
        ans = 0
        for r, c in enumerate(s):
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
            while d[c] > 1:
                d[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans