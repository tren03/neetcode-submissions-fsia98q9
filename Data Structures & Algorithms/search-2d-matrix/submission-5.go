func searchMatrix(matrix [][]int, target int) bool {
	/*
	Do bsearch for each row
	*/
	leftRow := 0
	rightRow := len(matrix)-1
	rowToCheck := 0
	exists := false


	for leftRow <= rightRow{
		mid := (leftRow + rightRow)/2
		if target >= matrix[mid][0] && target <= matrix[mid][len(matrix[0])-1]{
			rowToCheck = mid
			exists = true
			break
		}else if target > matrix[mid][len(matrix[0])-1]{
			leftRow = mid + 1
		}else{
			rightRow = mid - 1
		}
	}
	if exists == false{
		return false
	}

	left := 0
	right := len(matrix[0]) - 1

	for left <= right{
		mid := (left+right)/2
		cur := matrix[rowToCheck][mid]
		if cur == target{
			return true
		}else if cur < target{
			left = mid + 1
		}else{
			right = mid - 1
		}
	}
	return false
	

}
