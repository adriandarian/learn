#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Medium (31.01%)
# Likes:    14868
# Dislikes: 13897
# Total Accepted:    4.5M
# Total Submissions: 14.5M
# Testcase Example:  '123'
#
# Given a signed 32-bit integer x, return x with its digits reversed. If
# reversing x causes the value to go outside the signed 32-bit integer range
# [-2^31, 2^31 - 1], then return 0.
# 
# Assume the environment does not allow you to store 64-bit integers (signed or
# unsigned).
# 
# 
# Example 1:
# 
# 
# Input: x = 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: x = -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: x = 120
# Output: 21
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= x <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # Pythonic approach with sign preservation and bounds checking
        sign = -1 if x < 0 else 1
        reversed_num = int(str(abs(x))[::-1]) * sign
        
        # Check 32-bit signed integer bounds: [-2^31, 2^31 - 1]
        return reversed_num if -2**31 <= reversed_num <= 2**31 - 1 else 0
        
        # One-liner (most Pythonic):
        # sign = -1 if x < 0 else 1; rev = int(str(abs(x))[::-1]) * sign; return rev if -2**31 <= rev <= 2**31 - 1 else 0
        
        # True one-liner version (less readable):
        # return (lambda rev: rev if -2**31 <= rev <= 2**31 - 1 else 0)(int(str(abs(x))[::-1]) * (-1 if x < 0 else 1))
# @lc code=end

