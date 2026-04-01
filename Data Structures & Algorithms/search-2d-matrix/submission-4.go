func searchMatrix(matrix [][]int, target int) bool {
	/*
	Do bsearch for each row
	*/
	row := 0

	for row < len(matrix){
		left := 0
		right := len(matrix[0])-1
		curRow := matrix[row]
		fmt.Println(curRow)
		for left <= right{
			mid := (left+right)/2
			cur := curRow[mid]
			fmt.Println(cur)

			if cur == target{
				return true
			}else if cur < target{
				left = mid + 1
			}else{
				right = mid - 1
			}
		}
		row++
	}
	return false

}
