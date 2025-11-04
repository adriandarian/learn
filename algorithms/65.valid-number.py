#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#
# https://leetcode.com/problems/valid-number/description/
#
# algorithms
# Hard (22.15%)
# Likes:    1455
# Dislikes: 2196
# Total Accepted:    484.9K
# Total Submissions: 2.2M
# Testcase Example:  '"0"'
#
# Given a string s, return whether s is a valid number.
# 
# For example, all the following are valid numbers: "2", "0089", "-0.1",
# "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93",
# "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e",
# "e3", "99e2.5", "--6", "-+3", "95a54e53".
# 
# Formally, a valid number is defined using one of the following
# definitions:
# 
# 
# An integer number followed by an optional exponent.
# A decimal number followed by an optional exponent.
# 
# 
# An integer number is defined with an optional sign '-' or '+' followed by
# digits.
# 
# A decimal number is defined with an optional sign '-' or '+' followed by one
# of the following definitions:
# 
# 
# Digits followed by a dot '.'.
# Digits followed by a dot '.' followed by digits.
# A dot '.' followed by digits.
# 
# 
# An exponent is defined with an exponent notation 'e' or 'E' followed by an
# integer number.
# 
# The digits are defined as one or more digits.
# 
# 
# Example 1:
# 
# 
# Input: s = "0"
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "e"
# 
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: s = "."
# 
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 20
# s consists of only English letters (both uppercase and lowercase), digits
# (0-9), plus '+', minus '-', or dot '.'.
# 
# 
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s or s in ['+', '-', '.', 'e', 'E']:
            return False
        parts = s.lower().split('e')
        if len(parts) > 2 or any(not p for p in parts):
            return False
        if len(parts) == 2 and not (parts[1][0] in ['+', '-'] and len(parts[1]) > 1 or parts[1][0].isdigit()) or not all(c.isdigit() for c in (parts[1][1:] if parts[1][0] in ['+', '-'] else parts[1])):
            return False
        num_part = parts[0]
        if num_part[0] in ['+', '-']:
            num_part = num_part[1:]
        if not num_part or num_part == '.':
            return False
        dot_parts = num_part.split('.')
        if len(dot_parts) > 2:
            return False
        return all(p.isdigit() for p in dot_parts if p)
        
# @lc code=end

