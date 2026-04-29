import "slices"
func pacificAtlantic(heights [][]int) [][]int {
	m := len(heights)
	n := len(heights[0])
	//ans := make([][]int,0)
	var bfs func([][]int, [][]int) [][]int

	bfs = func(q [][]int, vis [][]int) [][]int{
		for _,v := range q{
			vis[v[0]][v[1]] = 1
		}
		for len(q) > 0{
			cur := q[0]
			q = slices.Delete(q,0,1)
			i := cur[0]
			j := cur[1]
			move := [][]int{{i+1,j},{i-1,j},{i,j+1},{i,j-1}}
			for _,v := range move{
				// only append if val index valid and val of index
				// smaller that cur, add node to ans
				if ((v[0] >= 0 && v[0] < m) && (v[1] >= 0 && v[1] < n)){
					if heights[v[0]][v[1]] >= heights[i][j] && vis[v[0]][v[1]] == 0{
						vis[v[0]][v[1]] = 1
						q = append(q, []int{v[0],v[1]})
					}
				}
			}
		}
		return vis
	}

	// seed for multisource bfs
	pSeed := make([][]int,0)
	aSeed := make([][]int,0)
	for i:=0;i<m;i+=1{
		for j:=0;j<n;j+=1{
			if i == 0 || j == 0{
				pSeed = append(pSeed,[]int{i,j})
			}
			if i == m-1 || j == n-1{
				aSeed = append(aSeed,[]int{i,j})
			}
		}
	}

	vis := make([][]int,len(heights))
	for ind,_ := range vis{
		vis[ind] = make([]int,len(heights[0]))
	}
	pVis := bfs(pSeed,vis)
	vis = make([][]int,len(heights))
	for ind,_ := range vis{
		vis[ind] = make([]int,len(heights[0]))
	}
	aVis := bfs(aSeed,vis)

	ans := make([][]int,0)
	fmt.Println(aVis)
	fmt.Println(pVis)

	for i, row:= range aVis{
		for j,_ := range row{
			if aVis[i][j] == 1{
				if aVis[i][j] == pVis[i][j]{
					ans = append(ans, []int{i,j})
				}
			}
		}
	}
	return ans
}
