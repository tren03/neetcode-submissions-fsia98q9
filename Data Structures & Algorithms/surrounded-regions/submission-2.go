import "slices"
func solve(board [][]byte) {
	m := len(board)
	n := len(board[0])
	vis := make([][]int, len(board))
	for ind,_ := range vis{
		vis[ind] = make([]int, len(board[0]))
	}
	q := make([][]int, 0)

	// seed q from borders for multisource bfs
	for i, row := range board{
		for j, _ := range row{
			if i == 0 || j == 0 || i == m-1 || j == n-1{
				if board[i][j] == 'O'{
					vis[i][j] = 1
					q = append(q, []int{i,j})
				}
			}
		}
	}

	for len(q) > 0{
		cur := q[0]
		q = slices.Delete(q, 0, 1)
		i := cur[0]
		j := cur[1]
		move := [][]int{{i+1,j},{i-1,j},{i,j+1},{i,j-1}}
		for _,d := range move{
			id := d[0]
			jd := d[1]

			if id >= 0 && id < m && jd >= 0 && jd < n{
				if board[id][jd] == 'O' && vis[id][jd] == 0{
					q = append(q, []int{id, jd})
					vis[id][jd] = 1
				}
			}
		}
	}

	fmt.Println(vis)
	for i, row := range board{
		for j, _ := range row{
			if board[i][j] == 'O' && vis[i][j] == 0{
				board[i][j] = 'X'
			}
		}
	}
	
	
    
}
