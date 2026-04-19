import "slices"
func bfs(i,j int, grid [][]int, vis [][]int, level int){
	q := make([][]int, 0)
	q = append(q, []int{i,j,level})
	for len(q) > 0{
		// append values, remove from first
		cur := q[0]
		q = slices.Delete(q, 0, 1)
		i := cur[0]
		j := cur[1]
		level := cur[2]
		// validations
		grid[i][j] = min(grid[i][j], level)
		fmt.Printf("marked %d %d with %d\n",i, j, min(grid[i][j], level))
		vis[i][j] = 1
		pd := [][]int{{i+1,j},{i-1,j},{i,j+1},{i,j-1}}
		for _,v := range pd{
			if v[0]>=len(grid) || v[0]<0{
				continue
			}
			if v[1]>=len(grid[0]) || v[1]<0{
				continue
			}
			i := v[0]
			j := v[1]
			if grid[i][j] == -1{
				continue
			}
			if vis[i][j] == 1{
				continue
			}
			q = append(q, []int{i,j,level+1})
		} 
	}
}
func islandsAndTreasure(grid [][]int) {
	// On reaching 0 - perfom DFS (keep vis array as soon as we start dfs)
	m := len(grid)
	n := len(grid[0])
	for i, ival := range grid{
		for j, jval := range ival{
			if jval == 0{
				fmt.Println("going in with", i, j)
				vis := make([][]int, m) 
				for ind, _ := range vis{
					vis[ind] = make([]int, n)
				}
				bfs(i,j, grid, vis,0)
			}
		}
	}
}