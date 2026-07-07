func validTree(n int, edges [][]int) bool {
	// buid adjaceny
	if len(edges) == 0{
		return true
	}
	adj := make(map[int][]int)
	visited := 0

	for _, e := range edges{
		parent := e[0]
		child := e[1]

		_, okParent := adj[parent]
		_, okChild := adj[child]
		if okParent{
			adj[parent] = append(adj[parent], child)
		}else{
			adj[parent] = []int{child}
		}

		if okChild{
			adj[child] = append(adj[child], parent)
		}else{
			adj[child] = []int{parent}
		}
	}
	vis := make([]int, n)
	fmt.Println(adj)

	q := make([][]int, 0) // parent | child
	q = append(q,[]int{-1, edges[0][0]})
	vis[edges[0][0]] = 1
	visited += 1

	for len(q) != 0{
		// pop que from first ele
		cur := q[0]
		parent := cur[0]
		toProcess := cur[1]
		q = q[1:]

		for _, neigh := range adj[toProcess]{
			if neigh != parent && vis[neigh] == 1{
				fmt.Println(parent,toProcess, neigh, vis)
				return false
			}else if vis[neigh]==0{
				visited += 1
				vis[neigh] = 1
				q = append(q, []int{toProcess,neigh})
			}
		}
	}
	if visited != n{
		return false
	}



	return true


}
