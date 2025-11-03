#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
# https://leetcode.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (65.29%)
# Likes:    10804
# Dislikes: 329
# Total Accepted:    938.1K
# Total Submissions: 1.4M
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# 
# A sudoku solution must satisfy all of the following rules:
# 
# 
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes
# of the grid.
# 
# 
# The '.' character indicates empty cells.
# 
# 
# Example 1:
# 
# 
# Input: board =
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output:
# [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is
# shown below:
# 
# 
# 
# 
# 
# Constraints:
# 
# 
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.
# 
# 
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Solve a Sudoku puzzle by filling empty cells in-place.
        
        Time Complexity: O(9^(n)) where n is the number of empty cells
        Space Complexity: O(1) - Only modifies the input board
        
        Algorithm: Backtracking with constraint propagation
        - For each empty cell, try digits 1-9
        - Check if digit is valid (row, column, 3x3 box)
        - Recursively solve; backtrack if no solution found
        """
        def is_valid(row: int, col: int, digit: str) -> bool:
            """Check if placing digit at (row, col) is valid"""
            # Check row
            if digit in board[row]:
                return False
            
            # Check column
            if any(board[i][col] == digit for i in range(9)):
                return False
            
            # Check 3x3 box
            box_row: int = (row // 3) * 3
            box_col: int = (col // 3) * 3
            if any(board[i][j] == digit for i in range(box_row, box_row + 3) for j in range(box_col, box_col + 3)):
                return False
            
            return True
        
        def solve() -> bool:
            """Backtracking solver - returns True when solved"""
            # Find next empty cell
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        # Try each digit 1-9
                        for digit in '123456789':
                            if is_valid(i, j, digit):
                                board[i][j] = digit
                                
                                # Recursively solve rest of board
                                if solve():
                                    return True
                                
                                # Backtrack if no solution found
                                board[i][j] = '.'
                        
                        return False
            
            # All cells filled - solved!
            return True
        
        solve()
        
        # Compact one-liner using nested lambdas (highly condensed):
        # (lambda solve: solve())((lambda self: (lambda f: f(lambda: next((f(lambda: any((board.__setitem__(i, j, digit), False)[-1] if not any(digit in board[i] or any(board[k][j] == digit for k in range(9)) or any(board[ii][jj] == digit for ii in range((i//3)*3, (i//3)*3+3) for jj in range((j//3)*3, (j//3)*3+3))) for digit in '123456789') for i in range(9) for j in range(9) if board[i][j] == '.'), None) or True)(lambda: all(board[i][j] != '.' for i in range(9) for j in range(9)))))(lambda: None))(self))
        
        # More readable alternative approach using generator:
        # (lambda solve: solve())((lambda: (lambda find_empty, is_valid, backtrack: backtrack())(
        #     lambda: next(((i, j) for i in range(9) for j in range(9) if board[i][j] == '.'), None),
        #     lambda i, j, d: not any(d in board[i] or any(board[k][j] == d for k in range(9)) or any(board[ii][jj] == d for ii in range((i//3)*3, (i//3)*3+3) for jj in range((j//3)*3, (j//3)*3+3))),
        #     lambda: (pos := find_empty()) and any(is_valid(pos[0], pos[1], d) and (board[pos[0].__setitem__(pos[1], d) or backtrack() or board[pos[0]].__setitem__(pos[1], '.')) for d in '123456789') or not pos
        # ))())
        
# @lc code=end

