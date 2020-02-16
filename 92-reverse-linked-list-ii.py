# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        tail = con = None
        # find m node
        index = 1
        current = head
        prev = None
        while current:
            if index == m:
                tail = current
                con = prev
                break

            prev = current
            current = current.next
            index += 1

        for _ in range(n - m + 1):
            _next = current.next
            current.next = prev
            prev = current
            current = _next

        if con:
            con.next = prev
        else:
            head = prev
        tail.next = current
        return head
