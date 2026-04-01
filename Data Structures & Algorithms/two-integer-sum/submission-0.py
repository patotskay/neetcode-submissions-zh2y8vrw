class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = 1
        d = {}
        while r != len(nums):
            d[nums[l]] = l  
            if target - nums[r] in d:
                return [d[target - nums[r]], r]  
            l += 1
            r += 1