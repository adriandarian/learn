class Solution:
    def solve(self, nums):
        nums.sort(reverse=True)
        return nums[0] * nums[1] if nums[0] * nums[1] > nums[-1] * nums[-2] else nums[-1] * nums[2]
