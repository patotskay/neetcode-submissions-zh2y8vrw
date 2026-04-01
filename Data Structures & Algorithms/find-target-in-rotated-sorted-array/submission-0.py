class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while r > l:
            m = (r + l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        left1 = l
        right1 = len(nums) - 1
        while right1 > left1:
            m = (right1 + left1) // 2
            if target > nums[m]:
                left1 = m + 1
            else:
                right1 = m
        if target == nums[left1]:
            return left1
        left2 = 0
        right2 = l
        while right2 > left2:
            m = (right2 + left2) // 2
            if target > nums[m]:
                left2 = m + 1
            else:
                right2 = m
        if target == nums[left2]:
            return left2
        return -1
