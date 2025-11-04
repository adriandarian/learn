#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#
# https://leetcode.com/problems/text-justification/description/
#
# algorithms
# Hard (49.52%)
# Likes:    4381
# Dislikes: 5270
# Total Accepted:    595.3K
# Total Submissions: 1.2M
# Testcase Example:  '["This", "is", "an", "example", "of", "text", "justification."]\n16'
#
# Given an array of strings words and a width maxWidth, format the text such
# that each line has exactly maxWidth characters and is fully (left and right)
# justified.
# 
# You should pack your words in a greedy approach; that is, pack as many words
# as you can in each line. Pad extra spaces ' ' when necessary so that each
# line has exactly maxWidth characters.
# 
# Extra spaces between words should be distributed as evenly as possible. If
# the number of spaces on a line does not divide evenly between words, the
# empty slots on the left will be assigned more spaces than the slots on the
# right.
# 
# For the last line of text, it should be left-justified, and no extra space is
# inserted between words.
# 
# Note:
# 
# 
# A word is defined as a character sequence consisting of non-space characters
# only.
# Each word's length is guaranteed to be greater than 0 and not exceed
# maxWidth.
# The input array words contains at least one word.
# 
# 
# 
# Example 1:
# 
# 
# Input: words = ["This", "is", "an", "example", "of", "text",
# "justification."], maxWidth = 16
# Output:
# [
# "This    is    an",
# "example  of text",
# "justification.  "
# ]
# 
# Example 2:
# 
# 
# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth =
# 16
# Output:
# [
# "What   must   be",
# "acknowledgment  ",
# "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall
# be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one
# word.
# 
# Example 3:
# 
# 
# Input: words =
# ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],
# maxWidth = 20
# Output:
# [
# "Science  is  what we",
# ⁠ "understand      well",
# "enough to explain to",
# "a  computer.  Art is",
# "everything  else  we",
# "do                  "
# ]
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 300
# 1 <= words[i].length <= 20
# words[i] consists of only English letters and symbols.
# 1 <= maxWidth <= 100
# words[i].length <= maxWidth
# 
# 
#

# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_line = []
        current_len = 0
        for word in words:
            if current_len + len(word) + len(current_line) > maxWidth:
                gaps = len(current_line) - 1
                spaces = maxWidth - current_len
                if gaps == 0:
                    result.append(current_line[0].ljust(maxWidth))
                else:
                    spaces_per_gap = spaces // gaps
                    extra_spaces = spaces % gaps
                    line = ''.join(w + ' ' * (spaces_per_gap + (1 if i < extra_spaces else 0)) for i, w in enumerate(current_line[:-1])) + current_line[-1]
                    result.append(line)
                current_line, current_len = [], 0
            current_line.append(word)
            current_len += len(word)
        result.append(' '.join(current_line).ljust(maxWidth))
        return result
        
# @lc code=end

