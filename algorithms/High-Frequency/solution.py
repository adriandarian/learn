from collections import Counter


class Solution:
    def solve(self, nums):
        return max(Counter(nums).values())
