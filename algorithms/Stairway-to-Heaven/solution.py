class Solution:
    def solve(self, nums):
        for i in range(len(nums)):
            nums[i] += i

        return nums
