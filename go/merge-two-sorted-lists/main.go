package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	dummy := &ListNode{Val: 0}
	tail := dummy
	for {
		if list1 == nil {
			tail.Next = list2
			break
		}
		if list2 == nil {
			tail.Next = list1
			break
		}

		if list1.Val <= list2.Val {
			tail.Next = list1
			list1 = list1.Next
		} else {
			tail.Next = list2
			list2 = list2.Next
		}
		tail = tail.Next
	}
	return dummy.Next
}
