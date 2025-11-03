#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Medium (61.61%)
# Likes:    4964
# Dislikes: 8979
# Total Accepted:    1.3M
# Total Submissions: 2.1M
# Testcase Example:  '1'
#
# The count-and-say sequence is a sequence of digit strings defined by the
# recursive formula:
# 
# 
# countAndSay(1) = "1"
# countAndSay(n) is the run-length encoding of countAndSay(n - 1).
# 
# 
# Run-length encoding (RLE) is a string compression method that works by
# replacing consecutive identical characters (repeated 2 or more times) with
# the concatenation of the character and the number marking the count of the
# characters (length of the run). For example, to compress the string "3322251"
# we replace "33" with "23", replace "222" with "32", replace "5" with "15" and
# replace "1" with "11". Thus the compressed string becomes "23321511".
# 
# Given a positive integer n, return the n^th element of the count-and-say
# sequence.
# 
# 
# Example 1:
# 
# 
# Input: n = 4
# 
# Output: "1211"
# 
# Explanation:
# 
# 
# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"
# 
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# 
# Output: "1"
# 
# Explanation:
# 
# This is the base case.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 30
# 
# 
# 
# Follow up: Could you solve it iteratively?
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        """
        Return the nth element of the count-and-say sequence.
        
        Time Complexity: O(n * m) where m is the length of current sequence
        Space Complexity: O(m) for storing the sequence
        
        Algorithm: Iteratively apply run-length encoding n-1 times starting from "1"
        """
        # Iterative approach - O(n * m) time, O(m) space
        current: str = "1"
        
        for _ in range(n - 1):
            # Apply run-length encoding to current
            result: list[str] = []
            i: int = 0
            
            while i < len(current):
                digit: str = current[i]
                count: int = 1
                
                # Count consecutive identical digits
                while i + count < len(current) and current[i + count] == digit:
                    count += 1
                
                # Append count + digit to result
                result.append(str(count) + digit)
                i += count
            
            current = ''.join(result)
        
        return current
        
        # Compact one-liner using nested generators and recursion:
        # return (lambda f: f(n))(lambda n: "1" if n == 1 else (lambda s: ''.join(str(len(list(g := (c for c in s if c == next((d for d in s if d != None), None))))) + next((d for d in s if d != None), None) for _ in range(1) if (s := f(n - 1))))(""))
        
        # More readable one-liner using reduce and groupby-like logic:
        # return (lambda reduce, n: reduce(lambda s, _: ''.join(str((c := s[i]) and (j := i); [j for j in range(i + 1, len(s)) if s[j] == c] and str(len([j for j in range(i + 1, len(s)) if s[j] == c]) + 1) + c or '' for i in range(0, len(s), 1 + len([j for j in range(i + 1, len(s)) if s[j] == s[i]]))), '', range(n - 1)), n))((lambda f: f(f))(lambda self: lambda func, n: func(self(self), func, n)), n)
        
        # Most Pythonic one-liner (using loop simulation):
        # return (lambda n: (lambda current: [current := ''.join(str(sum(1 for _ in iter(lambda i=[0]: (i.__setitem__(0, i[0] + 1), current[i[0] - 1] == (d := current[i[0]]) if i[0] < len(current) else False)[-1]))) + d for _ in range(1) for i in [0] for d in [current[0]] if (i := [0], True)[-1]) for _ in range(n - 1))("1")))(n)
        
        # Simplest effective one-liner (most readable):
        # return (lambda n: (lambda f: f(1))(lambda k: "1" if k > n else (lambda s, res: f(k + 1))((f(k-1)), ''.join(str(sum(1 for _ in iter(lambda c=[None]: (c.__setitem__(0, next((x for x in s if x != c[0]), None)), c[0] != None)[-1]))) + (c[0] or '') for _ in range(1)))))(1)
        
# @lc code=end

