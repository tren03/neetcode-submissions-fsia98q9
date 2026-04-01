/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reorderList(head *ListNode) {
	// split LL into 2
	// reverse second list
	// merge first and second 
	if head == nil{
		return
	}

	slow := head
	fast := head
	
	for {
		if fast.Next == nil{
			break
		} 
		if (fast.Next).Next == nil{
			break
		} 
		slow = slow.Next
		fast = (fast.Next).Next
	}
	if slow == fast{
		// only 1 ele
		return 
	}
	// head -> slow (first half)
	// slow.Next -> nil (second half)
	// Reverse second half

	second := slow.Next
	slow.Next = nil
	cur := second
	var prev *ListNode
	
	for cur != nil{
		temp := cur.Next
		cur.Next = prev
		prev = cur
		cur = temp
	}
	// prev would be the reversed head
	fmt.Println(head.Val,prev.Val)
	
	// merget the 2 lists 
	// 1 : head -> slow
	// 2 : prev -> nil

	p1, p2 := head, prev
	for p1 != nil && p2 != nil{
		// store so we do not lose it
		t1 := p1.Next

		// p1.Next should hold reversed list element
		p1.Next = p2

		// increment p1 so we can add more nodes
		p1 = p1.Next
		
		// increment p2 so we get a new reversed node next iter
		p2 = p2.Next

		// after adding reversed list node, we need to add the first node we saved of p1 
		p1.Next = t1
		
		// increment p1 so we can add more nodes
		p1 = p1.Next
	}
}
