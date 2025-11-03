#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (52.74%)
# Likes:    8938
# Dislikes: 15679
# Total Accepted:    2M
# Total Submissions: 3.7M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# 
# string convert(string s, int numRows);
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# 
# Example 2:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
# 
# Example 3:
# 
# 
# Input: s = "A", numRows = 1
# Output: "A"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: single row
        if numRows == 1:
            return s
        
        # Simulation approach - O(n) time, O(n) space
        rows = ['' for _ in range(numRows)]
        row, direction = 0, -1
        
        for char in s:
            rows[row] += char
            if row == 0 or row == numRows - 1:
                direction = -direction
            row += direction
        
        return ''.join(rows)
        
        # One-liner using modular arithmetic (pattern-based):
        # return ''.join(s[i::2*(numRows-1)] if idx in (0, numRows-1) else s[idx::2*(numRows-1)] + s[2*(numRows-1)-idx::2*(numRows-1)] for idx in range(numRows) for i in [idx])
        
        # More readable one-liner with cycle calculation:
        # cycle = 2 * (numRows - 1) if numRows > 1 else 1; return ''.join(s[i::cycle] if r == 0 or r == numRows - 1 else s[r::cycle][::2] + s[cycle - r::cycle][::2] for r in range(numRows) for i in [r] if cycle)  # Note: This version is cleaner
# @lc code=end

