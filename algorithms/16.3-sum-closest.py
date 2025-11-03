#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (47.48%)
# Likes:    11312
# Dislikes: 612
# Total Accepted:    1.6M
# Total Submissions: 3.5M
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an integer array nums of length n and an integer target, find three
# integers in nums such that the sum is closest to target.
# 
# Return the sum of the three integers.
# 
# You may assume that each input would have exactly one solution.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
# 
# 
# 
# Constraints:
# 
# 
# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Two-pointer approach after sorting - O(n²) time, O(1) space
        nums.sort()
        closest = sum(nums[:3])
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest if current sum is closer to target
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum
                
                # Move pointers based on sum vs target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  # Perfect match found
        
        return closest
        
        # One-liner using min with key (less efficient but Pythonic):
        # from itertools import combinations; return min((sum(combo) for combo in combinations(nums, 3)), key=lambda s: abs(s - target))
        
        # One-liner explanation: finds the 3-sum with minimum distance from target
# @lc code=end

