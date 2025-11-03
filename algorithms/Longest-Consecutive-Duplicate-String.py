#
# Longest consecutive duplicate string
#
# Given a string `s`, return the length of the longest substring with same characters.
#
# For example, given abcccdda, return 3 since it's the length of ccc.
#
# Example 1
#
# Input:
# s = "abbbba"
#
# Output:
# 4
#
# Example 2
#
# Input:
# s = "aaabbb"
#
# Output:
# 3
#

import itertools


class Solution:
    def solve(self, s):
        if not s:
            return 0
        return max(len(list(v)) for _, v in itertools.groupby(s))
