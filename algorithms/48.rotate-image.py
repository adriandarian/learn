#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
# https://leetcode.com/problems/rotate-image/description/
#
# algorithms
# Medium (78.81%)
# Likes:    19338
# Dislikes: 929
# Total Accepted:    2.6M
# Total Submissions: 3.2M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# You are given an n x n 2D matrix representing an image, rotate the image by
# 90 degrees (clockwise).
# 
# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# 
# 
# 
# Constraints:
# 
# 
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Rotate n x n matrix 90 degrees clockwise in-place.
        
        Time Complexity: O(n²)
        Space Complexity: O(1) - In-place rotation
        
        Algorithm: Transpose then reverse rows
        - Transpose: swap matrix[i][j] with matrix[j][i]
        - Reverse each row: reverses the order to achieve clockwise rotation
        """
        n: int = len(matrix)
        
        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()
        
        # One-liner combining both operations (highly Pythonic):
        # [matrix[i].__setitem__(j, matrix[j][i]) or matrix[j].__setitem__(i, matrix[i][j]) for i in range(n) for j in range(i + 1, n) if (matrix[i][j], matrix[j][i]) := (matrix[j][i], matrix[i][j])]
        # [row.reverse() for row in matrix]
        
        # Compact version using tuple unpacking and list comprehension:
        # _ = [[matrix[i].__setitem__(j, t), matrix[j].__setitem__(i, matrix[i][j]), matrix[i].__setitem__(j, t)] for i in range(len(matrix)) for j in range(i + 1, len(matrix)) if (t := matrix[i][j]) or True]
        # _ = [row.reverse() for row in matrix]
        
        # Pure one-liner (transpose + reverse as single operation):
        # _ = (lambda m: [m[i].__setitem__(j, m[j][i]) or m[j].__setitem__(i, m[i][j]) for i in range(len(m)) for j in range(i + 1, len(m))] or [m[i].reverse() for i in range(len(m))])(matrix)
        
        # Layer-by-layer rotation one-liner (alternative approach):
        # for layer in range(len(matrix) // 2):
        #     first, last = layer, len(matrix) - 1 - layer
        #     for i in range(first, last):
        #         offset = i - first
        #         top = matrix[first][i]
        #         matrix[first][i] = matrix[last - offset][first]
        #         matrix[last - offset][first] = matrix[last][last - offset]
        #         matrix[last][last - offset] = matrix[i][last]
        #         matrix[i][last] = top
        
# @lc code=end

