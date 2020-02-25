# https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1->2->2->1
# S
# F
# Stack = []

# 1->2->2->1
#    S
#       F
# Stack = [1]

# 1->2->2->1
#       S
#             F
# Stack = [1, 2]

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        stack = []
        slow = fast = head
        while fast is not None and fast.next is not None:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast is not None:
            slow = slow.next

        while slow is not None:
            if stack.pop() != slow.val:
                return False
            slow = slow.next

        return True
