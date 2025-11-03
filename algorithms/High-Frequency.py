#
# High frequency
#
# Given a list of integers `nums`, find the most frequently occurring element and return the **number of occurrences** of that element.
#
# For example, given the list [1, 4, 1, 7, 1, 7, 1, 1], return 5 since the the element 1 appears 5 times.
#
# Example 1
#
# Input:
# nums = [1, 4, 1, 7, 1, 7, 1, 1]
#
# Output:
# 5
#
# Example 2
#
# Input:
# nums = [5, 5, 5, 5, 5, 5, 5]
#
# Output:
# 7
#
# Example 3
#
# Input:
# nums = [1, 2, 3, 4, 5, 6, 7]
#
# Output:
# 1
#

from collections import Counter


class Solution:
    def solve(self, nums):
        return max(Counter(nums).values())
