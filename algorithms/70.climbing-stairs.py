#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (53.75%)
# Likes:    23871
# Dislikes: 997
# Total Accepted:    4.7M
# Total Submissions: 8.7M
# Testcase Example:  '2'
#
# You are climbing a staircase. It takes n steps to reach the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# 
# 
# Example 2:
# 
# 
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 45
# 
# 
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # Pythonic DP solution - O(n) time, O(1) space
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a
        
        # One-liner using reduce (functional programming style):
        # from functools import reduce; return reduce(lambda x, _: (x[1], x[0] + x[1]), range(n), (1, 1))[0]
        
        # Alternative one-liner using pow (matrix exponentiation - O(log n)):
        # m = [[1, 1], [1, 0]]; result = pow(m, n, None); return result[0][1] + result[1][1]
        # (Requires custom __pow__ for matrix class, so not practical as true one-liner)
# @lc code=end

