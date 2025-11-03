#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (58.41%)
# Likes:    11962
# Dislikes: 370
# Total Accepted:    1.5M
# Total Submissions: 2.6M
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sum to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note: The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Find all unique combinations in candidates where each number is used at most once.
        
        Time Complexity: O(2^n) where n is the length of candidates
        Space Complexity: O(n) for recursion depth
        
        Algorithm: Backtracking with sorting to handle duplicates
        - Sort candidates to group duplicates together
        - Skip duplicate candidates at same recursion level
        - Move to next index (no reuse) unlike Combination Sum I
        """
        result: list[list[int]] = []
        candidates.sort()  # Sort to group duplicates and enable early termination
        
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
                
                # Skip candidates equal to previous (avoid duplicates at same level)
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Early termination: if candidate > remaining, all following are larger
                if candidate > remaining:
                    break
                
                combo.append(candidate)
                # Move to next index (i+1) to prevent reuse
                backtrack(combo, remaining - candidate, i + 1)
                combo.pop()
        
        backtrack([], target, 0)
        return result
        
        # One-liner using nested lambda with duplicate skipping:
        # return (lambda backtrack: backtrack([], target, 0))(lambda combo, rem, start: result.append(combo[:]) if rem == 0 else [backtrack(combo + [candidates[i]], rem - candidates[i], i + 1) for i in range(start, len(candidates)) if candidates[i] <= rem and (i == start or candidates[i] != candidates[i - 1])])
        
        # Compact one-liner with generator (functional approach):
        # return (lambda f: f([], target, 0))(lambda combo, rem, start: [combo] if rem == 0 else [c for i in range(start, len(candidates)) if candidates[i] <= rem and (i == start or candidates[i] != candidates[i - 1]) for c in f(combo + [candidates[i]], rem - candidates[i], i + 1)])
        
        # Most Pythonic generator-based recursive one-liner:
        # def solve(combo, rem, start):
        #     return [combo] if rem == 0 else [c for i in range(start, len(candidates)) if (candidates[i] <= rem) and (i == start or candidates[i] != candidates[i-1]) for c in solve(combo + [candidates[i]], rem - candidates[i], i + 1)]
        # return solve([], target, 0)
        
# @lc code=end

