#
# Recurring Character
#
# Given a string, return the index of the first recurring character in it. If there are no recurring characters, return -1.
#
# Example 1
#
# Input:
# s = "abcda"
#
# Output:
# 4
#
# Explanation:
# The `a` at index 4 is the first recurring character.
#
# Example 2
#
# Input:
# s = "abcde"
#
# Output:
# -1
#
# Explanation:
# No recurring characters in this string.
#
# Example 3
#
# Input:
# s = "aaaaa"
#
# Output:
# 1
#
# Explanation:
# We want the first recurring character.
#

class Solution:
    def solve(self, s):
        for i in range(len(s)):
            if s[i] in s[:i]:
                return i

        return -1
