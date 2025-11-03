#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (47.73%)
# Likes:    22608
# Dislikes: 610
# Total Accepted:    3M
# Total Submissions: 6.3M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in non-decreasing order, find the
# starting and ending position of a given target value.
# 
# If target is not found in the array, return [-1, -1].
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """
        Find the starting and ending position of target in sorted array.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Algorithm: Two binary searches - one for leftmost, one for rightmost position
        """
        def binary_search_left(left: int, right: int) -> int:
            """Find leftmost position of target"""
            while left <= right:
                mid: int = (left + right) >> 1
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left if left < len(nums) and nums[left] == target else -1
        
        def binary_search_right(left: int, right: int) -> int:
            """Find rightmost position of target"""
            while left <= right:
                mid: int = (left + right) >> 1
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right if right >= 0 and nums[right] == target else -1
        
        if not nums:
            return [-1, -1]
        
        left_pos: int = binary_search_left(0, len(nums) - 1)
        
        # If target not found, return [-1, -1]
        if left_pos == -1:
            return [-1, -1]
        
        right_pos: int = binary_search_right(0, len(nums) - 1)
        return [left_pos, right_pos]
        
        # One-liner using list comprehension with binary search helper:
        # return (lambda f_left, f_right: [f_left, f_right] if f_left != -1 else [-1, -1])((lambda l, r: next((l for _ in iter(lambda: (mid := (l + r) >> 1) or nums[mid] < target and (l := mid + 1) or (r := mid - 1) if l <= r else None), None) or (l if l < len(nums) and nums[l] == target else -1)))(0, len(nums) - 1), (lambda l, r: next((r for _ in iter(lambda: (mid := (l + r) >> 1) or nums[mid] <= target and (l := mid + 1) or (r := mid - 1) if l <= r else None), None) or (r if r >= 0 and nums[r] == target else -1)))(0, len(nums) - 1)) if nums else [-1, -1]
        
        # Compact two-search one-liner (more readable):
        # return (lambda find_first, find_last: [find_first, find_last] if find_first != -1 else [-1, -1])((lambda l, r: (lambda _: l if l < len(nums) and nums[l] == target else -1)([nums.__setitem__(i, 1) for l, r in iter(lambda l=l, r=r: (l, r), (0, 0)) if l <= r for _ in iter(lambda: (m := (l + r) >> 1) or (l := m + 1) if nums[m] < target else (r := m - 1), None)]))(0, len(nums) - 1), (lambda l, r: (lambda _: r if r >= 0 and nums[r] == target else -1)([nums.__setitem__(i, 1) for l, r in iter(lambda l=l, r=r: (l, r), (0, 0)) if l <= r for _ in iter(lambda: (m := (l + r) >> 1) or (l := m + 1) if nums[m] <= target else (r := m - 1), None)]))(0, len(nums) - 1)) if nums else [-1, -1]
        
# @lc code=end

