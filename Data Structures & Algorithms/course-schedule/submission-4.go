import "slices"
func canFinish(numCourses int, prerequisites [][]int) bool {
	indeg := make([]int, (numCourses))
	graphState := make(map[int][]int)
	q := make([]int, 0)
	tp := 0

	for _, pre := range prerequisites{
		indeg[pre[0]] += 1
		_, ok := graphState[pre[1]]
		if !ok{
			graphState[pre[1]] = []int{pre[0]}
		}else{
			graphState[pre[1]] = append(graphState[pre[1]], pre[0])
		}
	}

	fmt.Println(indeg)

	for i,v := range indeg{
		if v == 0{
			q = append(q, i)
		}
	}

	for len(q) > 0{
		cur := q[0]
		q = slices.Delete(q,0,1)
		tp += 1

		// from graph state, for every neigh, reduce indeg.
		// if indgeg == 0, add to q
		neigh, _ := graphState[cur]

		for _,n := range neigh{
			indeg[n] -= 1
			if indeg[n] == 0{
				q = append(q, n)
			}
		}
	}

	return tp == numCourses


}
