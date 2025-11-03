#
# An anagram I am
#
# Given two strings `s0` and `s1`, return whether they are anagrams of each other. Two words are anagrams when you can rearrange one to become the other. For example, `"listen"` and `"silent"` are anagrams.
#
# Constraints:
# - Length of s0 and s1 is at most 5000.
#
# Example 1
#
# Input:
# s0 = "listen"
# s1 = "silent"
#
# Output:
# True
#
# Example 2
#
# Input:
# s0 = "bedroom"
# s1 = "bathroom"
#
# Output:
# False
#

class Solution:
    def solve(self, s0, s1):
        for i in s0:
            if i in s1:
                s0 = s0.replace(i, "", 1)
                s1 = s1.replace(i, "", 1)

        return len(s0) == 0 and len(s1) == 0
