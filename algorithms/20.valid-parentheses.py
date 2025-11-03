#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (43.11%)
# Likes:    26882
# Dislikes: 1954
# Total Accepted:    6.8M
# Total Submissions: 15.7M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "()"
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "()[]{}"
# 
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "(]"
# 
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: s = "([])"
# 
# Output: true
# 
# 
# Example 5:
# 
# 
# Input: s = "([)]"
# 
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # Stack-based approach - O(n) time, O(n) space
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}
        
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if not stack or pairs[stack.pop()] != char:
                    return False
        
        return not stack
        
        # One-liner using reduce (functional approach):
        # from functools import reduce; pairs = {'(': ')', '{': '}', '[': ']'}; return not reduce(lambda st, c: st + [c] if c in pairs else (st[:-1] if st and pairs[st[-1]] == c else None), s, [])
        
        # More practical one-liner with regex replacement:
        # import re; s_copy = s; s_new = re.sub(r'(\(\)|{}|\[\])', '', s); return not s_copy or (s_copy != s_new and not bool(re.sub(r'(\(\)|{}|\[\])', '', s_new)))
# @lc code=end

