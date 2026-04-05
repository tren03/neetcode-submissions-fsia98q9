/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
	m := make(map[*Node]*Node) // parent addr -> clone addr
	var ans *Node
	i := false
	for {
		cur := head
		if cur == nil{
			break
		}

        var curCopy *Node
        if t, ok := m[cur]; ok{
            curCopy = t
        }else{
		    curCopy = &Node{Val:cur.Val, Next:nil, Random:nil} // placeholder
		    m[cur] = curCopy
        }

		if i == false{
			ans = curCopy 
			i = true
		}

		// next pointer 
		if cur.Next == nil{
			curCopy.Next = nil
		}else if ptr, ok := m[cur.Next]; ok{
			curCopy.Next = ptr
		}else{
			nextClonePtr := &Node{Val:cur.Next.Val, Next:nil, Random:nil} 
			m[cur.Next] = nextClonePtr
			curCopy.Next = nextClonePtr
		}

		if cur.Random == nil{
			curCopy.Random = nil
		}else if ptr, ok := m[cur.Random]; ok{
			curCopy.Random = ptr
		}else{
            fmt.Println(cur.Random)
            randomClonePtr := &Node{Val:cur.Random.Val, Next:nil, Random:nil} // placeholder
            m[cur.Random] = randomClonePtr
            curCopy.Random = randomClonePtr
		}

		head = head.Next

	}
	return ans
}