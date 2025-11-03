#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (39.24%)
# Likes:    12516
# Dislikes: 1503
# Total Accepted:    1.5M
# Total Submissions: 3.8M
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers, return an array of all the unique
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 
# 
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 
# 
# You may return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Two nested loops + two-pointer approach - O(n³) time, O(1) space
        if len(nums) < 4:
            return []
        
        nums.sort()
        result = []
        
        for i in range(len(nums) - 3):
            # Optimization: if smallest 4 sum is too large, skip
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # Optimization: if largest 4 sum is too small, continue
            if nums[i] + nums[-3] + nums[-2] + nums[-1] < target:
                continue
            
            for j in range(i + 1, len(nums) - 2):
                # Similar optimizations for inner loop
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[-2] + nums[-1] < target:
                    continue
                
                # Two-pointer for remaining two numbers
                left, right = j + 1, len(nums) - 1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        # Skip duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        return result
        
        # One-liner using combinations (less efficient but Pythonic):
        # from itertools import combinations; return sorted(set(tuple(sorted(combo)) for combo in combinations(nums, 4) if sum(combo) == target))
# @lc code=end

