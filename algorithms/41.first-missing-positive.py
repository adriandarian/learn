#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (41.81%)
# Likes:    17971
# Dislikes: 1958
# Total Accepted:    1.6M
# Total Submissions: 3.8M
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array nums. Return the smallest positive integer
# that is not present in nums.
# 
# You must implement an algorithm that runs in O(n) time and uses O(1)
# auxiliary space.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
# 
# 
# Example 3:
# 
# 
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        """
        Find the smallest positive integer not present in array.
        
        Time Complexity: O(n)
        Space Complexity: O(1) - Uses in-place array manipulation
        
        Algorithm: Place each number in its "correct" position (value v at index v-1)
        - First pass: Place nums[i] at position nums[i]-1 if 1 <= nums[i] <= n
        - Second pass: Find first position where nums[i] != i+1
        - Answer is i+1, or n+1 if all positions correct
        """
        n: int = len(nums)
        
        # First pass: Place each number in its correct position
        # Number v should be at index v-1 (if 1 <= v <= n)
        for i in range(n):
            # Keep swapping until nums[i] is in correct position or can't be placed
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1]
                correct_idx: int = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        # Second pass: Find first position where value != index + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # All positions correct, answer is n + 1
        return n + 1
        
        # One-liner using sorted + enumerate (O(n log n) but Pythonic):
        # return next((i for i, val in enumerate(sorted(set(nums)), 1) if val != i), len(set(nums)) + 1) if nums else 1
        
        # Compact O(n) one-liner using generator with single pass simulation:
        # return next((i + 1 for i in range(len(nums)) if (lambda s: next((j for j in range(len(s)) if 1 <= s[j] <= len(s) and s[s[j]-1] != s[j]), None) and False or all(s[j] == j + 1 or s[j] != j + 1 for j in range(len(s))))(nums) and nums[i] != i + 1), len(nums) + 1)
        
        # Most Pythonic O(n) one-liner (sacrifices some clarity for O(1) space):
        # return (lambda n, s: next((i + 1 for i in range(n) if nums[i] != i + 1), n + 1))((lambda: ([(nums.__setitem__(i, nums[j]), nums.__setitem__(j, nums[i])) for i in range(len(nums)) for _ in iter(lambda j=i: (j := nums[i] - 1) if 1 <= nums[i] <= len(nums) and nums[nums[i]-1] != nums[i] else None, None)], len(nums))[1])(), len(nums))
        
        # Readable compressed version using two passes as list comprehensions:
        # _ = [nums.__setitem__(i, nums[j]) or nums.__setitem__(j, temp) for i in range(len(nums)) if 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i]-1] for j in [nums[i]-1] for temp in [nums[j]]]
        # return next((i + 1 for i in range(len(nums)) if nums[i] != i + 1), len(nums) + 1)
        
# @lc code=end

