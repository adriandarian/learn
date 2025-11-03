#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (81.26%)
# Likes:    20460
# Dislikes: 372
# Total Accepted:    2.8M
# Total Submissions: 3.5M
# Testcase Example:  '[1,2,3]'
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
# 
# 
#

# @lc code=start
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        Generate all possible permutations of given distinct integers.
        
        Time Complexity: O(n! * n) where n is length of nums
        Space Complexity: O(n!) for storing all permutations
        
        Algorithm: Backtracking - build permutations by choosing elements one by one
        - Use a visited set to track which elements are used
        - Build each permutation recursively
        - Add complete permutation to results when all elements are used
        """
        result: list[list[int]] = []
        
        def backtrack(perm: list[int], used: set[int]) -> None:
            """Recursively build permutations"""
            # Base case: all elements used
            if len(perm) == len(nums):
                result.append(perm[:])  # Add copy of current permutation
                return
            
            # Try each unused element
            for i in range(len(nums)):
                if i not in used:
                    perm.append(nums[i])
                    used.add(i)
                    
                    # Recurse
                    backtrack(perm, used)
                    
                    # Backtrack
                    perm.pop()
                    used.remove(i)
        
        backtrack([], set())
        return result
        
        # One-liner using nested lambda with backtracking (highly compressed):
        # return (lambda backtrack: backtrack([], set()))(lambda perm, used: result.append(perm[:]) if len(perm) == len(nums) else [backtrack(perm + [nums[i]], used | {i}) for i in range(len(nums)) if i not in used])
        
        # Compact one-liner with generator and recursion (functional):
        # return (lambda f: f([], set()))(lambda p, u: [p] if len(p) == len(nums) else [c for i in range(len(nums)) if i not in u for c in f(p + [nums[i]], u | {i})])
        
        # Most Pythonic generator-based one-liner (clean and efficient):
        # def solve(perm, used):
        #     return [perm] if len(perm) == len(nums) else [p for i in range(len(nums)) if i not in used for p in solve(perm + [nums[i]], used | {i})]
        # return solve([], set())
        
        # Pure functional one-liner using nested comprehension:
        # return [p for p in (lambda f: f([], set()))(lambda p, u: [p] if len(p) == len(nums) else [*[x for i in range(len(nums)) if i not in u for x in f(p + [nums[i]], u | {i})]])]
        
        # Iterative permutation one-liner (alternative without recursion):
        # from itertools import permutations  # Would violate no-import rule
        # return [list(p) for p in permutations(nums)]  # This is cheating, so commented
        
        # Compact iterative backtracking one-liner:
        # stk = [([], set())]
        # return [p for _ in iter(lambda: len(stk) > 0 and (perm := stk.pop())[1] if len((perm := stk.pop())) > 0 else None, None) if len(perm[0]) == len(nums) for p in [perm[0]] or (stk.extend([(perm[0] + [nums[i]], perm[1] | {i}) for i in range(len(nums)) if i not in perm[1]]) or [])]
        
# @lc code=end

