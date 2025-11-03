#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (71.67%)
# Likes:    21353
# Dislikes: 728
# Total Accepted:    4.2M
# Total Submissions: 5.9M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# 
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 
# Explanation:
# 
# 
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form
# each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to
# form each other.
# 
# 
# 
# Example 2:
# 
# 
# Input: strs = [""]
# 
# Output: [[""]]
# 
# 
# Example 3:
# 
# 
# Input: strs = ["a"]
# 
# Output: [["a"]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Group anagrams together from list of strings.
        
        Time Complexity: O(n * k log k) where n = len(strs), k = avg string length
        Space Complexity: O(n * k) for hash map
        
        Algorithm: Use sorted string as key
        - Sort each string to create canonical form (anagrams have same sorted form)
        - Group strings by their sorted form using dictionary
        - Return all groups
        """
        anagram_map: dict[str, list[str]] = {}
        
        for word in strs:
            # Sort word to get canonical form (all anagrams sort to same key)
            sorted_word: str = ''.join(sorted(word))
            
            # Add word to its anagram group
            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = []
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
        
        # One-liner using defaultdict simulation with setdefault (highly Pythonic):
        # return list((lambda d: [d.setdefault(''.join(sorted(w)), []).append(w) or d[''.join(sorted(w))] for w in strs] and d.values())({}))
        
        # Compact one-liner using dict comprehension with grouping:
        # return list({w := ''.join(sorted(s)): [x for x in strs if ''.join(sorted(x)) == w] for s in strs}.values())
        
        # Most efficient one-liner with single pass:
        # d = {}
        # return [d.setdefault(''.join(sorted(w)), []).append(w) or d[''.join(sorted(w))] for w in strs]
        # return list(d.values())
        
        # Pure functional one-liner using reduce (would need import):
        # from functools import reduce
        # return list(reduce(lambda d, w: d.update({(k := ''.join(sorted(w))): d.get(k, []) + [w]}) or d, strs, {}).values())
        
        # Alternative using setdefault in comprehension:
        # return list(set((lambda d: d.update({(''.join(sorted(w))): d.get(''.join(sorted(w)), []) + [w] for w in strs}) or d)({})).values() if False else (lambda d: [d.setdefault(''.join(sorted(w)), []).append(w) for w in strs] and list(d.values()))({}))
        
# @lc code=end

