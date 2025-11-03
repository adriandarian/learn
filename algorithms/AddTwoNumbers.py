#
# Add Two Numbers
#
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
# Javascript Submission
#
# Runtime: 108 ms, faster than 88.90% of JavaScript online submissions for Add Two Numbers.
# Memory Usage: 38.7 MB, less than 30.55% of JavaScript online submissions for Add Two Numbers.
#
# Python Submission
#
# Runtime: 60 ms, faster than 96.39% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    result = ListNode(0)
    result_tail = result
    carry = 0

    while l1 or l2 or carry:            
        val1  = (l1.val if l1 else 0)
        val2  = (l2.val if l2 else 0)
        carry, out = divmod(val1+val2 + carry, 10)    

        result_tail.next = ListNode(out)
        result_tail = result_tail.next                      

        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)

    return result.next
