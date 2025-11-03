#
# Even numbers
#
# Given a 2-dimensional list matrix, return the number of even numbers in the matrix.
#
# Example 1
#
# Input:
# matrix = [[1, 2, 8],
# [3, 5, 5],
# [4, 6, 6]]
#
# Output:
# 5
#
# Explanation:
# The even numbers are: 2, 8, 4, 6, and 6.
#

class Solution:
    def solve(self, matrix):
        count = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] % 2 == 0:
                    count += 1

        return count
