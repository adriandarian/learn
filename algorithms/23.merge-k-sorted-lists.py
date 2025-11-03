#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (58.04%)
# Likes:    20872
# Dislikes: 774
# Total Accepted:    2.7M
# Total Submissions: 4.7M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# You are given an array of k linked-lists lists, each linked-list is sorted in
# ascending order.
# 
# Merge all the linked-lists into one sorted linked-list and return it.
# 
# 
# Example 1:
# 
# 
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6
# 
# 
# Example 2:
# 
# 
# Input: lists = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: lists = [[]]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 10^4.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min-heap approach - O(N log k) time, O(k) space
        # N = total number of nodes, k = number of lists
        import heapq
        
        # Filter out None lists
        lists = [l for l in lists if l]
        if not lists:
            return None
        
        # Min heap: (value, unique_id, node)
        # unique_id needed because ListNode objects aren't comparable
        heap = [(l.val, i, l) for i, l in enumerate(lists)]
        heapq.heapify(heap)
        
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            val, idx, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            # Add next node from the same list to heap
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        
        return dummy.next
        
        # Alternative: Divide and Conquer (also O(N log k) time):
        # def mergeTwoLists(l1, l2):
        #     dummy = ListNode(0)
        #     curr = dummy
        #     while l1 and l2:
        #         if l1.val <= l2.val:
        #             curr.next = l1
        #             l1 = l1.next
        #         else:
        #             curr.next = l2
        #             l2 = l2.next
        #         curr = curr.next
        #     curr.next = l1 if l1 else l2
        #     return dummy.next
        # 
        # if not lists:
        #     return None
        # 
        # while len(lists) > 1:
        #     merged = []
        #     for i in range(0, len(lists), 2):
        #         l1 = lists[i]
        #         l2 = lists[i + 1] if i + 1 < len(lists) else None
        #         merged.append(mergeTwoLists(l1, l2))
        #     lists = merged
        # 
        # return lists[0]
        
        # One-liner using reduce (less efficient but Pythonic):
        # from functools import reduce; 
        # def merge2(l1, l2):
        #     return ListNode(0) if not l1 and not l2 else l1 if not l2 else l2 if not l1 else (l1.next := merge2(l1.next, l2), l1)[1] if l1.val <= l2.val else (l2.next := merge2(l1, l2.next), l2)[1]
        # return reduce(merge2, [l for l in lists if l]) if lists else None
# @lc code=end

