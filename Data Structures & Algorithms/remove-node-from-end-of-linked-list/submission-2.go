/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }

head -> 1 -> 2 -> 3


 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	if head == nil{
		return nil
	}
	var prev *ListNode
	counter := head
	length := 0
	for counter != nil{
		length += 1
		counter = counter.Next
	}
	fmt.Println(length)
	lengthFromStart := length - n
	cur := head

	for i := 1; i<= lengthFromStart; i++{
		temp := cur
		cur = cur.Next
		prev = temp
	}
	fmt.Println(prev, cur)

	if prev == nil{
		// remove first element
		head = head.Next
	}else{
		prev.Next = cur.Next
	}



	return head
}
