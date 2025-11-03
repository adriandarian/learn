#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (36.69%)
# Likes:    31749
# Dislikes: 1958
# Total Accepted:    4.3M
# Total Submissions: 11.6M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
# 
# 
# Example 1:
# 
# 
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Expand around center approach - O(n²) time, O(1) space
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        return max((expand(i, i) for i in range(len(s))), key=len) if len(s) == 1 else max(
            (expand(i, i) for i in range(len(s))) | {expand(i, i + 1) for i in range(len(s) - 1)}, key=len
        )
        
        # One-liner alternative (DP - O(n²) time, O(n²) space):
        # return max((s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1) if s[i:j] == s[i:j][::-1]), key=len)
        
        # Cleaner expand approach:
        # return max((s[i-d:i+d+1] for i in range(len(s)) for d in range(len(s)) if i-d >= 0 and i+d < len(s) and s[i-d:i+d+1] == s[i-d:i+d+1][::-1]), key=len, default=s[0])
        
# @lc code=end

