#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (64.79%)
# Likes:    20411
# Dislikes: 1106
# Total Accepted:    2.8M
# Total Submissions: 4.3M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any
# order.
# 
# A mapping of digits to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
# 
# 
# Example 1:
# 
# 
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 
# 
# Example 2:
# 
# 
# Input: digits = "2"
# Output: ["a","b","c"]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
# 
# 
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Handle empty input
        if not digits:
            return []
        
        # Phone keypad mapping
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        # Iterative approach using reduce (Pythonic)
        from functools import reduce
        return reduce(
            lambda acc, digit: [x + y for x in acc for y in phone_map[digit]],
            digits,
            ['']
        )
        
        # One-liner with reduce (same as above):
        # from functools import reduce; phone_map = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}; return reduce(lambda acc, d: [x + y for x in acc for y in phone_map[d]], digits, ['']) if digits else []
        
        # One-liner using itertools.product:
        # from itertools import product; phone_map = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}; return [''.join(combo) for combo in product(*(phone_map[d] for d in digits))] if digits else []
# @lc code=end

