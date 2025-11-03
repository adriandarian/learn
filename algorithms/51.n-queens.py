#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (74.23%)
# Likes:    13866
# Dislikes: 336
# Total Accepted:    1.1M
# Total Submissions: 1.5M
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
# 
# Given an integer n, return all distinct solutions to the n-queens puzzle. You
# may return the answer in any order.
# 
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space,
# respectively.
# 
# 
# Example 1:
# 
# 
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: [["Q"]]
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
    def solveNQueens(self, n: int) -> list[list[str]]:
        def solve(row: int, cols: set, diag1: set, diag2: set) -> list[list[str]]:
            return [[*map(lambda r: ''.join('Q' if cols_row[col] else '.' for col in range(n)), enumerate(board))] for board in (
                solve(row + 1, cols, diag1, diag2) if (
                    col := next((c for c in range(n) if c not in cols and row - c not in diag1 and row + c not in diag2), None)
                ) is None else solve(row + 1, cols | {col}, diag1 | {row - col}, diag2 | {row + col})
            ) if row == n else [[]]] if row < n else []
        
        def backtrack(row: int, cols: set, diag1: set, diag2: set, board: list[int]) -> list[list[str]]:
            if row == n:
                return [[''.join('Q' if board[r] == c else '.' for c in range(n)) for r in range(n)]]
            return [sol for col in range(n) if col not in cols and row - col not in diag1 and row + col not in diag2 for sol in backtrack(row + 1, cols | {col}, diag1 | {row - col}, diag2 | {row + col}, board + [col])]
        
        return backtrack(0, set(), set(), set(), [])
# @lc code=end

