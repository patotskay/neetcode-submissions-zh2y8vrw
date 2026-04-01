class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        max_length = 0
        max_c = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in d:
                d[s[r]] = 1
            else:
                d[s[r]] += 1
            max_c = max(max_c, d[s[r]])
            diff = (r - l + 1) - max_c
            if diff > k:
                d[s[l]] -= 1
                l += 1
            else:
                max_length = max(max_length, r - l + 1)
        return max_length