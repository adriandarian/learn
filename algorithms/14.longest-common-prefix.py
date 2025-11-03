#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (46.45%)
# Likes:    20285
# Dislikes: 4838
# Total Accepted:    5.1M
# Total Submissions: 11M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# 
# Example 1:
# 
# 
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.
# 
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Horizontal scanning with zip (most Pythonic)
        if not strs:
            return ""
        
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                return strs[0][:i]
        
        return min(strs, key=len)
        
        # One-liner using zip with all():
        # return "".join(c for c, *rest in zip(*strs) if all(x == c for x in rest)) if strs else ""
        
        # More readable one-liner with explicit iteration:
        # return "".join(c[0] for c in zip(*strs) if len(set(c)) == 1) if strs else ""
# @lc code=end

