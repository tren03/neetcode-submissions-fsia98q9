import "slices"
func orangesRotting(grid [][]int) int {
	q := make([][]int, 0)
	m := len(grid)
	n := len(grid[0])
	ans := 0
	freshCount := 0
	for i, row := range grid {
		for j, val := range row {
            fmt.Println(val)
			if val == 1 {
				freshCount += 1
			}
			if val == 2 {
				q = append(q,[]int{i, j, 0})
			}
		}
	}
	for len(q) > 0 {
		cur := q[0]
		i := cur[0]
		j := cur[1]
		level := cur[2]
		ans = level
		q = slices.Delete(q, 0, 1)

		// parse neighbours
		directions := [][]int{
			{i + 1, j},
			{i - 1, j},
			{i, j + 1},
			{i, j - 1},
		}
		for _, d := range directions {
			if (d[0] >= m || d[0] < 0) || (d[1] >= n || d[1] < 0) {
				continue
			} else {
				id := d[0]
				jd := d[1]
				if grid[id][jd] == 1 {
					grid[id][jd] = 2
					freshCount -= 1
					q = append(q,[]int{d[0], d[1], level + 1})
				}
			}
		}
	}
	if freshCount != 0 {
		return -1
	}
	return ans
}