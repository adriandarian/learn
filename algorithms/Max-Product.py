#
# Max Product
#
# Given a list of integers, find the largest product of two distinct elements.
#
# Example 1
#
# Input:
# nums = [5, 1, 7]
#
# Output:
# 35
#
# Explanation:
# 35 is the largest product that can be made from 5 * 7
#
# Example 2
#
# Input:
# nums = [7, 1, 7]
#
# Output:
# 49
#
# Explanation:
# 49 is the largest product that can be made from 7 * 7. The values can be the same but they must be separate elements.
#
# Example 3
#
# Input:
# nums = [-5, 1, -7]
#
# Output:
# 35
#
# Explanation:
# 35 is the largest product that can be made from -5 * -7.
#

class Solution:
    def solve(self, nums):
        nums.sort(reverse=True)
        return nums[0] * nums[1] if nums[0] * nums[1] > nums[-1] * nums[-2] else nums[-1] * nums[-2]
