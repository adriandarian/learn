#
# Take 5
#
# Given a array of integers `nums`, subtract 5 from every number in the array and return the array.
#
# For example, given the array [8, 3, 10, 15, 9], return [3, -2, 5, 10, 4].
#
# Example 1
#
# Input:
# nums = [8, 3, 10, 15, 9]
#
# Output:
# [3, -2, 5, 10, 4]
#

class Solution:
    def solve(self, nums):
        return list(map(lambda x: x - 5, nums))
