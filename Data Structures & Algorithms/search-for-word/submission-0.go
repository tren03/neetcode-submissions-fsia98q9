func exist(board [][]byte, word string) bool {
    vis := make([][]int, len(board))
    for ind,_ := range vis{
        vis[ind] = make([]int, len(board[0]))
    }
    var dfs func(int,int,[][]int,string) bool
    dfs = func(i,j int, vis [][]int, tword string) bool{
        if len(tword) <= 0{
            return true
        }
        if board[i][j] != tword[0] || vis[i][j] == 1{
            return false
        }
        vis[i][j] = 1
        tword = tword[1:]
        if len(tword) <= 0{
            return true
        }
        flag := false
        prob := [][]int{{i+1,j},{i-1,j},{i,j+1},{i,j-1}}
        for _,d := range prob{
            di := d[0]
            dj := d[1]
            if (di >= 0 && di < len(board)) && (dj >= 0 && dj < len(board[0])){
                t := dfs(di,dj,vis,tword)
                if t == true{
                    flag = true
                    break
                }
            }
        }
        vis[i][j]=0
        return flag
    }

    for i,row := range board{
        for j,_ := range row{
            if board[i][j] == word[0]{
               tempAns := dfs(i,j,vis,word) 
               if tempAns == true{
                    return true
               }
            }
        }
    }
    return false
}