func isValidSudoku(board [][]byte) bool {
	row := make([]map[byte]int, 9)
	col := make([]map[byte]int, 9)
	box := make([]map[byte]int, 9)

	// initialize
	for i := 0;i< 9;i++{
		row[i] = make(map[byte]int)
		col[i] = make(map[byte]int)
		box[i] = make(map[byte]int)
	}

	for i := 0;i< 9;i++{
		for j:=0; j<9; j++{
			val := board[i][j]
			if val == '.'{
				continue
			}
			row[i][val] += 1
			col[j][val] += 1

			iB := i / 3
			jB := j / 3
			boxIndex := (jB * 3) + iB
			box[boxIndex][val] += 1

			if row[i][val] > 1 || col[j][val] > 1 || box[boxIndex][val] > 1{
				return false
			}


	}
	}
	return true

	}

