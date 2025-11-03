#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (45.09%)
# Likes:    31176
# Dislikes: 3499
# Total Accepted:    3.8M
# Total Submissions: 8.4M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
# 
# The overall run time complexity should be O(log (m+n)).
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# 
# 
# 
# Constraints:
# 
# 
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Binary search solution - O(log(min(m,n))) time complexity
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            cut1 = (left + right) // 2
            cut2 = (m + n + 1) // 2 - cut1
            
            left_1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            right_1 = float('inf') if cut1 == m else nums1[cut1]
            left_2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            right_2 = float('inf') if cut2 == n else nums2[cut2]
            
            if left_1 <= right_2 and left_2 <= right_1:
                return (max(left_1, left_2) + min(right_1, right_2)) / 2 if (m + n) % 2 == 0 else max(left_1, left_2)
            elif left_1 > right_2:
                right = cut1 - 1
            else:
                left = cut1 + 1
        
        # One-liner (simple but O(n+m) - not optimal):
        # merged = sorted(nums1 + nums2); n = len(merged); return (merged[n//2] + merged[(n-1)//2]) / 2
# @lc code=end

