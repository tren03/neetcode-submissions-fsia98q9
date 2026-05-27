import "slices"
func findOrder(numCourses int, prerequisites [][]int) []int {
	/* 
	We store the graph like this
	{
		0 - 1,2
		1 - 3,4
	}
	*/

	g := make(map[int][]int)
	indeg := make([]int,numCourses)
	q := make([]int,0)
	vis := make([]int, numCourses)
	ans := make([]int,0)
	for _, pre := range prerequisites{
		if _,ok := g[pre[1]]; ok{
			g[pre[1]] = append(g[pre[1]],pre[0])
			indeg[pre[0]] += 1
			continue
		}
		t := make([]int,0)
		indeg[pre[0]] += 1
		g[pre[1]] = t
		g[pre[1]] = append(g[pre[1]],pre[0])
	}
	for i,v := range indeg{
		if v == 0{
			q = append(q, i)
			vis[i] = 1
		}
	}
	fmt.Println(indeg)
	for len(q) > 0{
		toProcess := q[0]
		q = slices.Delete(q, 0, 1)
		ans = append(ans, toProcess)

		neig := g[toProcess]
		for _,n := range neig{
			indeg[n] -= 1
			if vis[n] == 0 && indeg[n] == 0{
				q = append(q, n)
				vis[n] = 1
			}
		}
	}
	if len(ans) != numCourses{
		return []int{}
	}
	return ans
    
}
