#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (77.85%)
# Likes:    22802
# Dislikes: 1062
# Total Accepted:    2.6M
# Total Submissions: 3.4M
# Testcase Example:  '3'
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 8
# 
# 
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Backtracking approach - O(4^n / sqrt(n)) time (Catalan number)
        result = []
        
        def backtrack(current: str, open_count: int, close_count: int) -> None:
            # Base case: valid combination found
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Add opening bracket if we haven't used all n
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            
            # Add closing bracket if it won't exceed opening brackets
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)
        
        backtrack('', 0, 0)
        return result
        
        # One-liner using generator and recursion (functional):
        # def gen(n, open=0, close=0, s=''):
        #     if len(s) == 2*n: yield s
        #     if open < n: yield from gen(n, open+1, close, s+'(')
        #     if close < open: yield from gen(n, open, close+1, s+')')
        # return list(gen(n))
        
        # One-liner with nested function (more compact):
        # f = lambda n: (lambda g: g(n, 0, 0, ''))(lambda n, o, c, s: [s] if len(s)==2*n else (g(n,o+1,c,s+'(') if o<n else [])+(g(n,o,c+1,s+')') if c<o else []))
        # Note: This becomes unreadable, so the backtracking version is recommended
# @lc code=end

