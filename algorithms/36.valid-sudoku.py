#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
# https://leetcode.com/problems/valid-sudoku/description/
#
# algorithms
# Medium (63.68%)
# Likes:    12165
# Dislikes: 1245
# Total Accepted:    2.3M
# Total Submissions: 3.6M
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:
# 
# 
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
# without repetition.
# 
# 
# Note:
# 
# 
# A Sudoku board (partially filled) could be valid but is not necessarily
# solvable.
# Only the filled cells need to be validated according to the mentioned
# rules.
# 
# 
# 
# Example 1:
# 
# 
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner
# being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it
# is invalid.
# 
# 
# 
# Constraints:
# 
# 
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.
# 
# 
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        Validate a 9x9 Sudoku board (partially filled).
        
        Time Complexity: O(1) - Fixed 9x9 board, constant iterations
        Space Complexity: O(1) - Fixed size data structures
        
        Algorithm: Check rows, columns, and 3x3 boxes for digit uniqueness
        """
        # Three sets to track seen digits: rows, columns, boxes
        seen_rows: dict[int, set[str]] = {i: set() for i in range(9)}
        seen_cols: dict[int, set[str]] = {j: set() for j in range(9)}
        seen_boxes: dict[tuple[int, int], set[str]] = {(i, j): set() for i in range(3) for j in range(3)}
        
        for i in range(9):
            for j in range(9):
                cell: str = board[i][j]
                
                if cell == '.':
                    continue
                
                # Check if digit already exists in row, column, or box
                if cell in seen_rows[i] or cell in seen_cols[j]:
                    return False
                
                # Calculate 3x3 box coordinates
                box_key: tuple[int, int] = (i // 3, j // 3)
                if cell in seen_boxes[box_key]:
                    return False
                
                # Add digit to all three tracking structures
                seen_rows[i].add(cell)
                seen_cols[j].add(cell)
                seen_boxes[box_key].add(cell)
        
        return True
        
        # One-liner using nested list comprehensions (Pythonic):
        # return not any(len(cells) != len(set(cells)) for cells in [[board[i][j] for i in range(9) for j in range(9) if board[i][j] != '.' and ((i == row and j < 9) or (j == col and i < 9) or (i // 3 == box_row and j // 3 == box_col))] for row in range(9) for col in range(9) for box_row in range(3) for box_col in range(3)])
        
        # Compact one-liner checking all constraints:
        # return all(len(cells) == len(set(cells)) for group_type in ['rows', 'cols', 'boxes'] for cells in (([board[i][j] for j in range(9) if board[i][j] != '.'] for i in range(9)) if group_type == 'rows' else ([board[i][j] for i in range(9) if board[i][j] != '.'] for j in range(9)) if group_type == 'cols' else ([board[i][j] for i in range(box_row*3, box_row*3+3) for j in range(box_col*3, box_col*3+3) if board[i][j] != '.'] for box_row in range(3) for box_col in range(3))))
        
        # Most Pythonic one-liner using generator with all():
        # return all(len(cells := [board[i][j] for i in range(9) if board[i][j] != '.' and (j == col and i < 9)]) == len(set(cells)) for col in range(9)) and all(len(cells := [board[i][j] for j in range(9) if board[i][j] != '.' and (i == row and j < 9)]) == len(set(cells)) for row in range(9)) and all(len(cells := [board[i][j] for i in range(br*3, br*3+3) for j in range(bc*3, bc*3+3) if board[i][j] != '.']) == len(set(cells)) for br in range(3) for bc in range(3))
        
# @lc code=end

