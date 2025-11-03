#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#
# https://leetcode.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (77.61%)
# Likes:    4189
# Dislikes: 281
# Total Accepted:    543.8K
# Total Submissions: 700.6K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
# 
# Given an integer n, return the number of distinct solutions to the n-queens
# puzzle.
# 
# 
# Example 1:
# 
# 
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as
# shown.
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 9
# 
# 
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int, cols: set, diag1: set, diag2: set) -> int:
            return sum(backtrack(row + 1, cols | {col}, diag1 | {row - col}, diag2 | {row + col}) for col in range(n) if col not in cols and row - col not in diag1 and row + col not in diag2) if row < n else 1
        return backtrack(0, set(), set(), set())
# @lc code=end

