/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func hasCycle(head *ListNode) bool {
	if head == nil{
		return false
	}
	slow := head
	fast := head.Next

	for {
		if fast == nil{
			return false
		}
		if fast.Next == nil{
			return false
		}

		// move fast twice 
		fast = (fast.Next).Next

		// move slow once
		slow = slow.Next

		if slow == fast{
			return true
		}
	}
	return false


    
}
