#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
# https://leetcode.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (30.79%)
# Likes:    8945
# Dislikes: 402
# Total Accepted:    794.8K
# Total Submissions: 2.6M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement wildcard pattern
# matching with support for '?' and '*' where:
# 
# 
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
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
# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# 
# 
# Example 3:
# 
# 
# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not
# match 'b'.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length, p.length <= 2000
# s contains only lowercase English letters.
# p contains only lowercase English letters, '?' or '*'.
# 
# 
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Wildcard pattern matching with '?' (single char) and '*' (any sequence).
        
        Time Complexity: O(m * n) where m and n are lengths of s and p
        Space Complexity: O(m * n) for DP table
        
        Algorithm: Dynamic Programming approach
        - dp[i][j] = True if s[0:i] matches p[0:j]
        - '?' matches exactly one character
        - '*' matches zero or more characters
        """
        m: int = len(s)
        n: int = len(p)
        
        # DP table: dp[i][j] means s[0:i] matches p[0:j]
        dp: list[list[bool]] = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like *, **, *** at the beginning
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' matches zero chars: dp[i][j-1]
                    # '*' matches one or more chars: dp[i-1][j]
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # '?' or exact match: check previous position
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]
        
        # Greedy two-pointer approach (O(m*n) time, O(1) space - commented):
        # s_idx: int = 0
        # p_idx: int = 0
        # star_idx: int = -1
        # match: int = 0
        #
        # while s_idx < m:
        #     if p_idx < n and (p[p_idx] == '?' or p[p_idx] == s[s_idx]):
        #         s_idx += 1
        #         p_idx += 1
        #     elif p_idx < n and p[p_idx] == '*':
        #         star_idx = p_idx
        #         match = s_idx
        #         p_idx += 1
        #     elif star_idx != -1:
        #         p_idx = star_idx + 1
        #         match += 1
        #         s_idx = match
        #     else:
        #         return False
        #
        # while p_idx < n and p[p_idx] == '*':
        #     p_idx += 1
        #
        # return p_idx == n
        
        # One-liner using nested DP with reduce simulation (highly condensed):
        # return (lambda dp: dp[m][n])((lambda: (dp := [[False] * (n + 1) for _ in range(m + 1)], [dp[0].__setitem__(0, True)] + [dp[0].__setitem__(j, dp[0][j-1] if p[j-1] == '*' else False) for j in range(1, n + 1)] + [[dp[i].__setitem__(j, (dp[i][j-1] if p[j-1] == '*' else False) or (dp[i-1][j] if j > 0 and p[j-1] == '*' else False) or (dp[i-1][j-1] if j > 0 and (p[j-1] == '?' or s[i-1] == p[j-1]) else False)) for j in range(1, n + 1)] for i in range(1, m + 1)], dp)[2])())
        
        # More readable one-liner using list comprehension with manual DP:
        # return (lambda dp: dp[m][n])([[(i == 0 and j == 0) or (j > 0 and p[j-1] == '*' and (dp[i][j-1] or (i > 0 and dp[i-1][j]))) or (j > 0 and i > 0 and (p[j-1] == '?' or s[i-1] == p[j-1]) and dp[i-1][j-1]) for j in range(n + 1)] for i in range(m + 1)])
        
        # Compact functional version using reduce (would need import, so alternative):
        # def solve(s, p):
        #     dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        #     dp[0][0] = True
        #     for j in range(1, len(p) + 1):
        #         if p[j-1] == '*':
        #             dp[0][j] = dp[0][j-1]
        #     for i in range(1, len(s) + 1):
        #         for j in range(1, len(p) + 1):
        #             if p[j-1] == '*':
        #                 dp[i][j] = dp[i][j-1] or dp[i-1][j]
        #             elif p[j-1] == '?' or s[i-1] == p[j-1]:
        #                 dp[i][j] = dp[i-1][j-1]
        #     return dp[m][n]
        # return solve(s, p)
        
# @lc code=end

