class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        def fulfill_dict(a, b):
            for ch in a:
                if ch not in b:
                    b[ch] = 1
                else:
                    b[ch] += 1
            return b
        fulfill_dict(s, d1)
        fulfill_dict(t, d2)
        return True if d1 == d2 else False


