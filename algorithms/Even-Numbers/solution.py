class Solution:
    def solve(self, matrix):
        count = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] % 2 == 0:
                    count += 1

        return count
