    /**
    * Definition for a Node.
    * type Node struct {
    *     Val int
    *     Neighbors []*Node
    * }
    */
	import "slices"

    func cloneGraph(node *Node) *Node {
        if node == nil{
            return nil
        }
        m := make(map[int]*Node, 0)
        var ans *Node
        stack := make([]*Node, 0)
        stack = append(stack, node)

        for len(stack) > 0{
            // check if node in map, else create
            var cloned *Node
            top := stack[len(stack)-1]
            stack = slices.Delete(stack, len(stack)-1, len(stack))
            if n, ok := m[top.Val]; ok{
                cloned = n
            }else{
                cloned = &Node{
                    Val: top.Val,
                    Neighbors: []*Node{},
                }
                m[top.Val] = cloned
            }

            if cloned.Val == 1{
                ans = cloned
            }
			/*
            for _, v := range stack{
                fmt.Println(*v)
            }
            fmt.Println("stack")
            fmt.Println(m)
            fmt.Println("\n")*/

            // neighs
            for _, neighPtr := range top.Neighbors{
                if clonedNeighbor, ok := m[neighPtr.Val]; ok{
                    cloned.Neighbors = append(cloned.Neighbors, clonedNeighbor)
                }else{
                    clonedNeighbor := &Node{
                        Val: neighPtr.Val,
                        Neighbors: []*Node{},
                    }
                    m[neighPtr.Val] = clonedNeighbor
                    cloned.Neighbors = append(cloned.Neighbors, clonedNeighbor)
                    stack = append(stack, neighPtr)
                }
            }
        }
        return ans
    }