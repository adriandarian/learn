#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (29.89%)
# Likes:    13041
# Dislikes: 2354
# Total Accepted:    1.3M
# Total Submissions: 4.2M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string s and a pattern p, implement regular expression
# matching with support for '.' and '*' where:
# 
# 
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# 
# 
# The matching should cover the entire input string (not partial).
# 
# 
# Example 1:
# 
# 
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
# 
# 
# Example 3:
# 
# 
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a
# previous valid character to match.
# 
# 
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Dynamic Programming approach - O(m*n) time and space
        memo = {}
        
        def dp(si: int, pi: int) -> bool:
            if (si, pi) in memo:
                return memo[(si, pi)]
            
            # Base cases
            if pi == len(p):
                return si == len(s)
            
            # Check if current characters match
            match = si < len(s) and p[pi] in {'.', s[si]}
            
            # Handle '*' pattern
            if pi + 1 < len(p) and p[pi + 1] == '*':
                # Either skip the pattern (zero repetitions) or use it (one or more)
                result = dp(si, pi + 2) or (match and dp(si + 1, pi))
            else:
                result = match and dp(si + 1, pi + 1)
            
            memo[(si, pi)] = result
            return result
        
        return dp(0, 0)
        
        # One-liner using Python's re module (NOT the intended solution, but Pythonic):
        # import re; return bool(re.fullmatch(p, s))
        
        # True algorithmic one-liner (difficult to read):
        # memo = {}; f = lambda si, pi: si == len(s) if pi == len(p) else ((memo.get((si, pi), (False, (lambda m: m or (si < len(s) and p[pi] in {'.', s[si]} and f(si + 1, pi + 2 if pi + 1 < len(p) and p[pi + 1] == '*' else pi + 1)))(si < len(s) and p[pi] in {'.', s[si]}))), None))[0] if (si, pi) in memo else (memo.update({(si, pi): (si < len(s) and p[pi] in {'.', s[si]}) if pi + 1 >= len(p) or p[pi + 1] != '*' else f(si, pi + 2) or (si < len(s) and p[pi] in {'.', s[si]} and f(si + 1, pi))}), memo[(si, pi)])[1]); return f(0, 0)
# @lc code=end

