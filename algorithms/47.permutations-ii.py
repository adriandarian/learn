#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (62.43%)
# Likes:    8987
# Dislikes: 158
# Total Accepted:    1.2M
# Total Submissions: 1.9M
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers, nums, that might contain duplicates, return
# all possible unique permutations in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
# 
# 
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        """
        Generate all unique permutations of array with possible duplicates.
        
        Time Complexity: O(n! * n) where n is length of nums
        Space Complexity: O(n!) for storing unique permutations
        
        Algorithm: Backtracking with sorting and duplicate skipping
        - Sort array to group duplicates together
        - Use visited array to track which indices are used
        - Skip duplicate elements at same recursion level
        - Build permutations recursively
        """
        result: list[list[int]] = []
        nums.sort()  # Sort to enable duplicate skipping
        visited: list[bool] = [False] * len(nums)
        
        def backtrack(perm: list[int]) -> None:
            """Recursively build unique permutations"""
            # Base case: built complete permutation
            if len(perm) == len(nums):
                result.append(perm[:])  # Add copy
                return
            
            # Try each element
            for i in range(len(nums)):
                # Skip if already used
                if visited[i]:
                    continue
                
                # Skip duplicates: only use first occurrence at each level
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                
                visited[i] = True
                perm.append(nums[i])
                
                # Recurse
                backtrack(perm)
                
                # Backtrack
                perm.pop()
                visited[i] = False
        
        backtrack([])
        return result
        
        # One-liner using nested lambda with duplicate handling (highly compressed):
        # return (lambda backtrack: (nums.sort() or backtrack([], [False] * len(nums))))(lambda perm, visited: result.append(perm[:]) if len(perm) == len(nums) else [backtrack(perm + [nums[i]], visited) for i in range(len(nums)) if not visited[i] and not (i > 0 and nums[i] == nums[i-1] and not visited[i-1]) and (visited.__setitem__(i, True), backtrack(perm + [nums[i]], visited), visited.__setitem__(i, False), None)[-1]])
        
        # Compact generator-based one-liner (functional, cleaner):
        # return (lambda f: f([], [False] * len(nums)))(lambda p, v: [p] if len(p) == len(nums) else [c for i in range(len(nums)) if not v[i] and not (i > 0 and nums[i] == nums[i-1] and not v[i-1]) for c in (v.__setitem__(i, True), f(p + [nums[i]], v), v.__setitem__(i, False), [])[2]]) if (nums.sort() or True) else []
        
        # Most Pythonic one-liner using helper function (readable):
        # nums.sort()
        # def solve(perm, visited):
        #     return [perm] if len(perm) == len(nums) else [c for i in range(len(nums)) if not visited[i] and not (i > 0 and nums[i] == nums[i-1] and not visited[i-1]) for c in (visited.__setitem__(i, True), solve(perm + [nums[i]], visited), visited.__setitem__(i, False), [])[2]]
        # return solve([], [False] * len(nums))
        
        # Alternative using set to track duplicates (less efficient but readable):
        # return (lambda f: f([], set()))(lambda p, used: [p] if len(p) == len(nums) else [c for i in range(len(nums)) if i not in used and (i == 0 or nums[i] != nums[i-1] or all(nums[j] != nums[i] for j in range(i) if j not in used)) for c in f(p + [nums[i]], used | {i})])
        
        # Iterative approach one-liner (stack-based):
        # return (lambda: [p for st in [[([], set())]] if st for perm, used in iter(lambda: st.pop() if st else None, None) for _ in [st.extend([(perm + [nums[i]], used | {i}) for i in range(len(nums)) if i not in used and (i == 0 or nums[i] != nums[i-1] or not any(j < i and j not in used for j in range(i) if nums[j] == nums[i]))])] if len(perm) == len(nums) else [] for p in [perm]])()
        
# @lc code=end

