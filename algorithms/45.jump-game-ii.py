#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Medium (42.08%)
# Likes:    16067
# Dislikes: 689
# Total Accepted:    1.9M
# Total Submissions: 4.6M
# Testcase Example:  '[2,3,1,1,4]'
#
# You are given a 0-indexed array of integers nums of length n. You are
# initially positioned at index 0.
# 
# Each element nums[i] represents the maximum length of a forward jump from
# index i. In other words, if you are at index i, you can jump to any index (i
# + j) where:
# 
# 
# 0 <= j <= nums[i] and
# i + j < n
# 
# 
# Return the minimum number of jumps to reach index n - 1. The test cases are
# generated such that you can reach index n - 1.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1
# step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,3,0,1,4]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].
# 
# 
#

# @lc code=start
class Solution:
    def jump(self, nums: list[int]) -> int:
        """
        Find minimum number of jumps to reach the last index.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Algorithm: Greedy approach - track farthest reachable position
        - Maintain current jump's end and farthest position reachable
        - When reaching current jump's end, increment jumps and extend range
        - Continue until reaching or passing the last index
        """
        jumps: int = 0
        current_end: int = 0  # End of range for current jump
        farthest: int = 0     # Farthest position reachable so far
        
        # Process all positions except the last (already reachable)
        for i in range(len(nums) - 1):
            # Update farthest position reachable from current position
            farthest = max(farthest, i + nums[i])
            
            # If reached end of current jump range, make a jump
            if i == current_end:
                jumps += 1
                current_end = farthest
        
        return jumps
        
        # Compact one-liner using reduce simulation (functional approach):
        # return (lambda: (jumps := 0, current_end := 0, farthest := 0) and sum(1 for i in range(len(nums) - 1) if (farthest := max(farthest, i + nums[i])) or (jumps := jumps + 1, current_end := farthest)[0] if i == current_end else False))[-1] if nums else 0
        
        # Pythonic one-liner using nested variables (walrus operator):
        # return sum(1 for i in range(len(nums) - 1) if i == (ce := 0) or (i >= ce and (jumps := 1, ce := max(range(ce, len(nums) - 1), key=lambda j: j + nums[j]) if i < len(nums) - 2 else len(nums) - 1, False) or jumps))
        
        # Most readable compact version with helper function:
        # def min_jumps(nums):
        #     jumps = current_end = farthest = 0
        #     for i in range(len(nums) - 1):
        #         farthest = max(farthest, i + nums[i])
        #         if i == current_end:
        #             jumps += 1
        #             current_end = farthest
        #     return jumps
        # return min_jumps(nums)
        
        # True one-liner (though hard to read):
        # return (lambda n: (lambda f: f(0, 0, 0, len(n) - 1))(lambda i, je, f, ln: je if i >= ln else (lambda new_f: f(i + 1, je + 1 if i == je else je, max(f, i + n[i]), ln) if i == je else f(i + 1, je, new_f, ln))(max(f, i + n[i])))(nums)
        
# @lc code=end

