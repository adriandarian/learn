#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (49.99%)
# Likes:    18150
# Dislikes: 864
# Total Accepted:    4.3M
# Total Submissions: 8.5M
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array of distinct integers and a target value, return the
# index if the target is found. If not, return the index where it would be if
# it were inserted in order.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,3,5,6], target = 7
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums contains distinct values sorted in ascending order.
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        """
        Find index of target in sorted array, or insertion position if not found.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Algorithm: Binary search to find exact match or insertion point
        """
        # Binary search approach - O(log n) time, O(1) space
        left: int = 0
        right: int = len(nums) - 1
        
        while left <= right:
            mid: int = (left + right) >> 1  # Bitwise right shift for division by 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # left will be at the insertion position
        return left
        
        # One-liner using nested lambda (functional approach):
        # return (lambda f: f(0, len(nums) - 1))(lambda l, r: l if l > r else (mid := (l + r) >> 1) or (mid if nums[mid] == target else f(l, mid + 1) if nums[mid] < target else f(l, mid - 1)))
        
        # Compact one-liner with walrus operator (Python 3.8+, enhanced for 3.14):
        # return next((i for i, n in enumerate(nums) if n >= target), len(nums)) if not target in nums else next(i for i, n in enumerate(nums) if n == target)
        
        # Note: The above one-liner is O(n), so we use the O(log n) binary search above
        
# @lc code=end

