#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (59.83%)
# Likes:    15009
# Dislikes: 2876
# Total Accepted:    7.2M
# Total Submissions: 12M
# Testcase Example:  '121'
#
# Given an integer x, return true if x is a palindrome, and false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# 
# 
# Example 2:
# 
# 
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a
# palindrome.
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= x <= 2^31 - 1
# 
# 
# 
# Follow up: Could you solve it without converting the integer to a string?
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # One-liner: String reversal approach (most Pythonic)
        return str(x) == str(x)[::-1]
        
        # One-liner: Negative numbers always fail (still string approach):
        # return x >= 0 and str(x) == str(x)[::-1]
        
        # Mathematical approach (solves follow-up - no string conversion):
        # return x >= 0 and x == self._reverse_int(x)
        # def _reverse_int(self, x):
        #     rev = 0
        #     while x > 0:
        #         rev = rev * 10 + x % 10
        #         x //= 10
        #     return rev
        
        # One-liner mathematical (lambda):
        # return x >= 0 and (lambda f: f(x, 0))(lambda n, r: n == 0 or (n == r or n // 10 == r and f(n // 10, r * 10 + n % 10)))
# @lc code=end

