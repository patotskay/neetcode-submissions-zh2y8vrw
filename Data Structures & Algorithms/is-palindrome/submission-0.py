class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = "".join(s1 for s1 in s if s1.isalnum())
        ans1 = ans.lower()
        n = len(ans1)
        l = 0
        r = n - 1  
        while l <= r:
            if ans1[r] == ans1[l]:
                l += 1
                r -= 1
            else:
                return False
        return True
