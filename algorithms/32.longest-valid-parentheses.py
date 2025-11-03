#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (37.31%)
# Likes:    13071
# Dislikes: 457
# Total Accepted:    996.4K
# Total Submissions: 2.7M
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', return the length
# of the longest valid (well-formed) parentheses substring.
# 
# 
# Example 1:
# 
# 
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# 
# 
# Example 2:
# 
# 
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# 
# 
# Example 3:
# 
# 
# Input: s = ""
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 3 * 10^4
# s[i] is '(', or ')'.
# 
# 
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        Find the length of the longest valid (well-formed) parentheses substring.
        
        Uses dynamic programming with O(n) time and O(n) space complexity.
        dp[i] represents the length of longest valid parentheses ending at index i.
        """
        # DP approach - O(n) time, O(n) space
        if not s or len(s) < 2:
            return 0
        
        dp: list[int] = [0] * len(s)
        max_len: int = 0
        
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0)
                max_len = max(max_len, dp[i])
        
        return max_len
        
        # Two-pass scanning approach (Pythonic alternative):
        # left = right = max_len = 0
        # for char in s:
        #     if char == '(':
        #         left += 1
        #     else:
        #         right += 1
        #     if left == right:
        #         max_len = max(max_len, right * 2)
        #     elif right > left:
        #         left = right = 0
        # 
        # left = right = 0
        # for char in reversed(s):
        #     if char == '(':
        #         left += 1
        #     else:
        #         right += 1
        #     if left == right:
        #         max_len = max(max_len, left * 2)
        #     elif left > right:
        #         left = right = 0
        # return max_len
        
        # One-liner using stack-based approach (compressed):
        # return (lambda: max(((stack := [], [stack.append(i) for i, c in enumerate(s) if c == '('] or [stack.pop() if stack and s[i] == ')' else stack.append(i) for i in range(len(s)) if s[i] == ')'] or (max(i - stack[-1] if stack else i + 1 for i in range(len(s))) if stack else 0))[-1], 0))() if s else 0
        
# @lc code=end

