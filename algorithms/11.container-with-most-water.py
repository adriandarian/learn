#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (58.93%)
# Likes:    32890
# Dislikes: 2112
# Total Accepted:    4.7M
# Total Submissions: 8M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the i^th line are (i, 0) and (i,
# height[i]).
# 
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
# 
# Return the maximum amount of water a container can store.
# 
# Notice that you may not slant the container.
# 
# 
# Example 1:
# 
# 
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.
# 
# 
# Example 2:
# 
# 
# Input: height = [1,1]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two-pointer approach - O(n) time, O(1) space
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate current area
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
        
        # One-liner using reduce (functional approach):
        # from functools import reduce; return reduce(lambda m, _: max(m, (r - l) * min(height[l], height[r]) if (l := l + 1 if height[l] < height[r] else l) or True else (r := r - 1)), range(len(height) - 1), 0)
        # Note: Walrus operator `:=` in lambdas is tricky, so better avoided
        
        # More practical one-liner with manual loop tracking:
        # return max((width := right - left) * min(height[left], height[right]) for right in range(len(height) - 1, 0, -1) if (left := next((i for i in range(right) if height[i] * (right - i) >= max((right - j) * height[j] for j in range(right))), 0)) or True)
# @lc code=end

