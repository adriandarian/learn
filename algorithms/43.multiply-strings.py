#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (43.00%)
# Likes:    7561
# Dislikes: 3606
# Total Accepted:    1.1M
# Total Submissions: 2.5M
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
# 
# Note: You must not use any built-in BigInteger library or convert the inputs
# to integer directly.
# 
# 
# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# 
# 
# Constraints:
# 
# 
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
# 
# 
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Multiply two large numbers represented as strings without direct conversion.
        
        Time Complexity: O(m * n) where m and n are lengths of num1 and num2
        Space Complexity: O(m + n) for result array
        
        Algorithm: Grade-school multiplication with digit-by-digit multiplication
        - For each digit pair, multiply and add to appropriate positions
        - Handle carries manually
        - Convert result array to string
        """
        # Handle edge case
        if num1 == "0" or num2 == "0":
            return "0"
        
        m: int = len(num1)
        n: int = len(num2)
        result: list[int] = [0] * (m + n)
        
        # Reverse iteration for easier indexing (rightmost digits first)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Multiply digits at positions i and j
                digit1: int = int(num1[i])
                digit2: int = num2[j]
                
                # Product contributes to positions i+j and i+j+1
                mul: int = digit1 * digit2
                pos1: int = i + j  # Position for carries
                pos2: int = i + j + 1  # Position for current digit
                
                total: int = mul + result[pos2]
                result[pos2] = total % 10
                result[pos1] += total // 10
        
        # Convert result array to string, skip leading zeros
        result_str: str = ''.join(map(str, result))
        return result_str.lstrip('0') or "0"
        
        # One-liner using nested loops and accumulation (Pythonic):
        # return (lambda res: (lambda: [res.__setitem__(i + j + 1, (res[i + j + 1] + int(num1[i]) * int(num2[j])) % 10) or res.__setitem__(i + j, res[i + j] + (res[i + j + 1] + int(num1[i]) * int(num2[j])) // 10) for i in range(len(num1) - 1, -1, -1) for j in range(len(num2) - 1, -1, -1)])() or ''.join(map(str, res)).lstrip('0') or '0')([0] * (len(num1) + len(num2)))
        
        # More readable one-liner using reduce (would require import, so alternative):
        # Compact version with explicit multiplication table approach:
        # return (lambda n1, n2: (lambda t: ''.join(map(str, t)).lstrip('0') or '0')([0] * (len(n1) + len(n2))) if n1 == '0' or n2 == '0' else (lambda res: (res := [0] * (len(n1) + len(n2)), [(res.__setitem__(i + j + 1, (res[i + j + 1] + int(n1[i]) * int(n2[j])) % 10), res.__setitem__(i + j, res[i + j] + (res[i + j + 1] + int(n1[i]) * int(n2[j])) // 10)) for i in range(len(n1) - 1, -1, -1) for j in range(len(n2) - 1, -1, -1)], ''.join(map(str, res)).lstrip('0') or '0'])[-1])(num1, num2)
        
        # Most Pythonic one-liner (pure functional, converts to int internally):
        # return str(int(num1) * int(num2))  # This violates the constraint, so commented
        
        # Best readable one-liner without imports:
        # return (lambda res: ''.join(map(str, res)).lstrip('0') or '0')((lambda: [res := [0] * (len(num1) + len(num2)) or [(res.__setitem__(i + j + 1, (res[i + j + 1] + int(num1[i]) * int(num2[j])) % 10), res.__setitem__(i + j, res[i + j] + (res[i + j + 1] + int(num1[i]) * int(num2[j])) // 10)) for i in range(len(num1) - 1, -1, -1) for j in range(len(num2) - 1, -1, -1)] or res][1])()) if num1 != '0' and num2 != '0' else '0'
        
# @lc code=end

