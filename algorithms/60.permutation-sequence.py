#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence/description/
#
# algorithms
# Hard (51.11%)
# Likes:    7121
# Dislikes: 498
# Total Accepted:    520.6K
# Total Submissions: 1M
# Testcase Example:  '3\n3'
#
# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
# 
# By listing and labeling all of the permutations in order, we get the
# following sequence for n = 3:
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# Given n and k, return the k^th permutation sequence.
# 
# 
# Example 1:
# Input: n = 3, k = 3
# Output: "213"
# Example 2:
# Input: n = 4, k = 9
# Output: "2314"
# Example 3:
# Input: n = 3, k = 1
# Output: "123"
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 9
# 1 <= k <= n!
# 
# 
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1] * (n + 1)
        for i in range(2, n + 1): factorial[i] = factorial[i - 1] * i
        k -= 1
        numbers = list(range(1, n + 1))
        result = []
        for i in range(n, 0, -1):
            idx = k // factorial[i - 1]
            result.append(str(numbers.pop(idx)))
            k %= factorial[i - 1]
        return ''.join(result)
        
# @lc code=end

