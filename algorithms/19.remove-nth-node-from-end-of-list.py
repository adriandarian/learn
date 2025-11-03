#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (50.19%)
# Likes:    20703
# Dislikes: 881
# Total Accepted:    3.8M
# Total Submissions: 7.6M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, remove the n^th node from the end of the
# list and return its head.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [1], n = 1
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: head = [1,2], n = 1
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
# 
# 
# 
# Follow up: Could you do this in one pass?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two-pointer approach (one-pass) - O(L) time, O(1) space
        # Create dummy node to handle edge case of removing head
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # Move right pointer n steps ahead
        for _ in range(n):
            right = right.next
        
        # Move both pointers until right reaches end
        while right:
            left = left.next
            right = right.next
        
        # Remove the nth node
        left.next = left.next.next
        
        return dummy.next
        
        # One-liner approach (two-pass with list conversion):
        # nodes = []; curr = head; [nodes.append(curr) or curr := curr.next for _ in range(30) if curr]; nodes.pop(len(nodes) - n) if n <= len(nodes) else None; return head if n > 1 else (head.next if head else None) if n == len(nodes) else head
        # Note: This is complex and not recommended; the two-pointer approach is cleaner
# @lc code=end

