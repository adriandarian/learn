#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (75.55%)
# Likes:    20481
# Dislikes: 513
# Total Accepted:    2.8M
# Total Submissions: 3.7M
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen
# numbers sum to target. You may return the combinations in any order.
# 
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen
# numbers is different.
# 
# The test cases are generated such that the number of unique combinations that
# sum up to target is less than 150 combinations for the given input.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple
# times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# 
# 
# Example 3:
# 
# 
# Input: candidates = [2], target = 1
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Find all unique combinations of candidates that sum to target.
        
        Time Complexity: O(N^(T/M)) where N is candidates length, T is target, M is minimum candidate
        Space Complexity: O(T/M) for recursion depth
        
        Algorithm: Backtracking with unlimited candidate reuse
        """
        result: list[list[int]] = []
        
        def backtrack(combo: list[int], remaining: int, start: int) -> None:
            """Recursive backtracking to find all valid combinations"""
            if remaining == 0:
                result.append(combo[:])  # Add copy of current combination
                return
            
            if remaining < 0:
                return
            
            # Try each candidate starting from 'start' index
            for i in range(start, len(candidates)):
                candidate: int = candidates[i]
                
                if candidate <= remaining:
                    combo.append(candidate)
                    # Reuse same index to allow unlimited repetition
                    backtrack(combo, remaining - candidate, i)
                    combo.pop()
        
        backtrack([], target, 0)
        return result
        
        # One-liner using nested lambda with backtracking:
        # return (lambda backtrack: backtrack([], target, 0))(lambda combo, rem, start: result.append(combo[:]) if rem == 0 else [backtrack(combo + [candidates[i]], rem - candidates[i], i) for i in range(start, len(candidates)) if candidates[i] <= rem])
        
        # Compact one-liner using generator and recursion:
        # return (lambda f: f([], target, 0))(lambda combo, rem, start: [result.append(combo)] if rem == 0 else [[f(combo + [c], rem - c, i), 0][-1] for i, c in enumerate(candidates[start:], start) if c <= rem])
        
        # Most Pythonic generator-based one-liner (functional):
        # return list((lambda f: f([], target, 0))(lambda combo, rem, start: (combo,) if rem == 0 else (item for i in range(start, len(candidates)) for item in f(combo + [candidates[i]], rem - candidates[i], i) if candidates[i] <= rem)))
        
        # Simplified readable one-liner using list comprehension with recursion:
        # def solve(combo, rem, start):
        #     return [combo] if rem == 0 else [c for i in range(start, len(candidates)) if candidates[i] <= rem for c in solve(combo + [candidates[i]], rem - candidates[i], i)]
        # return solve([], target, 0)
        
# @lc code=end

