/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	ans := &ListNode{}
	pointer := ans
	for {
		//fmt.Println(list1.Val, list2.Val, ans.Val)
		fmt.Println(ans.Val)
		if list1 != nil && list2 != nil{
			if list1.Val <= list2.Val{
				ans.Next = list1
				ans = ans.Next
				list1 = list1.Next
			}else{
				ans.Next = list2
				ans = ans.Next
				list2 = list2.Next
			}
		}else{
			break
		}
	}

	for list1 != nil{
		ans.Next = list1
		ans = list1
		list1 = list1.Next
	}

	for list2 != nil{
		ans.Next = list2
		ans = list2
		list2 = list2.Next
	}

	return pointer.Next
    
}
