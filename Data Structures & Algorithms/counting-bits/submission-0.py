class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = [0] * (n + 1)
        
        for i in range(n + 1):
            cnt = 0
            num = i
            while num != 0:
                num = num & (num - 1)
                cnt += 1
            ans[i] = cnt
        
        return ans
        