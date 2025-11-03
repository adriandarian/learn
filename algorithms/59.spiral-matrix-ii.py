#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (74.16%)
# Likes:    6793
# Dislikes: 280
# Total Accepted:    743.8K
# Total Submissions: 1M
# Testcase Example:  '3'
#
# Given a positive integer n, generate an n x n matrix filled with elements
# from 1 to n^2 in spiral order.
# 
# 
# Example 1:
# 
# 
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: [[1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 20
# 
# 
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        num, top, bottom, left, right = 1, 0, n - 1, 0, n - 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1): matrix[top][i] = (num := num + 1) - 1
            top += 1
            for i in range(top, bottom + 1): matrix[i][right] = (num := num + 1) - 1
            right -= 1
            if top <= bottom:
                for i in range(right, left - 1, -1): matrix[bottom][i] = (num := num + 1) - 1
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1): matrix[i][left] = (num := num + 1) - 1
                left += 1
        return matrix
        
# @lc code=end

