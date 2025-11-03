#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (43.61%)
# Likes:    29067
# Dislikes: 1763
# Total Accepted:    4M
# Total Submissions: 9.2M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# There is an integer array nums sorted in ascending order (with distinct
# values).
# 
# Prior to being passed to your function, nums is possibly left rotated at an
# unknown index k (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
# (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices
# and become [4,5,6,7,0,1,2].
# 
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Find target index in a rotated sorted array using binary search.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Algorithm:
        1. Perform binary search while tracking which side is sorted
        2. If left side is sorted and target is in range, search left
        3. Otherwise search right side
        """
        # Binary search approach - O(log n) time, O(1) space
        left: int = 0
        right: int = len(nums) - 1
        
        while left <= right:
            mid: int = (left + right) >> 1  # Bitwise right shift for division by 2
            
            if nums[mid] == target:
                return mid
            
            # Determine which side is sorted
            if nums[left] <= nums[mid]:  # Left side is sorted
                # Check if target is in sorted left range
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # Right side is sorted
                # Check if target is in sorted right range
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
        
        # One-liner recursive approach (Pythonic):
        # return (lambda f: f(0, len(nums) - 1))(lambda l, r: -1 if l > r else (mid := (l + r) >> 1) or (nums[mid] if nums[mid] == target else (f(l, mid - 1) if nums[l] <= target < nums[mid] else f(mid + 1, r) if (nums[l] <= nums[mid]) else (f(mid + 1, r) if nums[mid] < target <= nums[r] else f(l, mid - 1)))))
        
        # Compact one-liner using walrus operator (Python 3.8+, enhanced for 3.14):
        # return next((i for i, n in enumerate(nums) if n == target), -1) if target in nums else -1
        
        # Note: The above one-liner is O(n), so we use the O(log n) binary search above
        
# @lc code=end

