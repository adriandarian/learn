class Solution:
    def solve(self, nums):
        return sum(nums) - (len(nums) * (len(nums) - 1) / 2)
