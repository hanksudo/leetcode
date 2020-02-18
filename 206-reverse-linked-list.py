# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        prev = None
        current = head
        while current:
            _next = current.next
            current.next = prev
            prev = current
            current = _next
        return prev
