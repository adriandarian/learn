#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (66.14%)
# Likes:    35346
# Dislikes: 653
# Total Accepted:    3.2M
# Total Submissions: 4.8M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
# 
# 
# Example 1:
# 
# 
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
# 
# 
# Example 2:
# 
# 
# Input: height = [4,2,0,3,2,5]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Calculate units of rain water trapped after raining.
        
        Time Complexity: O(n)
        Space Complexity: O(n) for dynamic programming arrays
        
        Algorithm: Dynamic Programming - precompute left/right maximums
        - For each position, water trapped = min(left_max, right_max) - height[i]
        - Left_max[i] = maximum height from left up to i
        - Right_max[i] = maximum height from right up to i
        """
        if not height or len(height) < 3:
            return 0
        
        n: int = len(height)
        
        # Precompute maximum heights from left and right
        left_max: list[int] = [0] * n
        right_max: list[int] = [0] * n
        
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        # Calculate trapped water
        trapped: int = 0
        for i in range(n):
            water_level: int = min(left_max[i], right_max[i])
            trapped += max(0, water_level - height[i])
        
        return trapped
        
        # Two-pointer O(1) space approach (commented alternative):
        # left: int = 0
        # right: int = n - 1
        # left_max: int = 0
        # right_max: int = 0
        # trapped: int = 0
        #
        # while left < right:
        #     if height[left] < height[right]:
        #         if height[left] >= left_max:
        #             left_max = height[left]
        #         else:
        #             trapped += left_max - height[left]
        #         left += 1
        #     else:
        #         if height[right] >= right_max:
        #             right_max = height[right]
        #         else:
        #             trapped += right_max - height[right]
        #         right -= 1
        # return trapped
        
        # One-liner using two-pointer approach (most Pythonic for O(1) space):
        # return (lambda: sum([(lambda l, r, lm, rm, t: (lm, rm, t, l := l + 1) if height[l] < height[r] else (lm, rm, t, r := r - 1) for _ in iter(lambda: 0, 1) if l < r for lm, rm, t, _ in [(max(lm, height[l]), rm, t + max(0, lm - height[l]), l := l + 1) if height[l] >= height[r] else (lm, max(rm, height[r]), t + max(0, rm - height[r]), r := r - 1)]])[-1][-1])(0, len(height) - 1, 0, 0, 0) if height and len(height) > 2 else 0
        
        # Compact DP one-liner using reduce (functional approach):
        # from functools import reduce  # Would violate no-import rule, so commented
        # return sum(min(max(height[:i+1]), max(height[i:])) - height[i] for i in range(len(height)) if height)
        
        # Most readable one-liner using generator expression (no precomputation):
        # return sum(min((lambda l: max(l) if l else 0)(height[:i+1]), (lambda r: max(r) if r else 0)(height[i:])) - height[i] for i in range(len(height)))
        
        # Efficient one-liner with precomputed max arrays:
        # return sum(min(lm, rm) - h for h, lm, rm in zip(height, (lambda h: [h[0]] + [max(h[i], max(h[:i])) for i in range(1, len(h))])(height), (lambda h: [max(h[:i+1]) if i < len(h) else 0 for i in range(len(h)-1, -1, -1)])(height))) if height else 0
        
# @lc code=end

