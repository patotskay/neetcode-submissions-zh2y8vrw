class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set_nums = set(nums)
        ans = 0
        for num in set_nums:
            if num - 1 not in set_nums:
                current_length = 1
                current_num = num
                while current_num + 1 in set_nums:
                    current_length += 1
                    current_num += 1
                ans = max(ans, current_length)
        return ans