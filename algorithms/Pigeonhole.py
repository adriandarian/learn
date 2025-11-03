#
# Pigeonhole
#
# You are given an array of length `n + 1` picked from the range 1, 2, ..., n. By the pigeonhole principle,
# there must be a duplicate. Find and return it. There is guaranteed to be exactly one duplicate.
#
# Bonus: Can you do this in linear time and constant space?
#
# Example 1
#
# Input:
# nums = [1, 2, 3, 1]
#
# Output:
# 1
#
# Example 2
#
# Input:
# nums = [4, 2, 1, 3, 2]
#
# Output:
# 2
#

class Solution:
    def solve(self, nums):
        return sum(nums) - (len(nums) * (len(nums) - 1) / 2)
