func dfs(m int, n int, i int, j int, visited [][]bool, grid [][]int, area *int) {
    if (i > m-1 || i < 0) || (j > n-1 || j < 0) || visited[i][j] == true || grid[i][j] == 0{
        return
    }
    *area += 1
    visited[i][j] = true
    dfs(m,n,i+1,j,visited,grid,area)
    dfs(m,n,i-1,j,visited,grid,area)
    dfs(m,n,i,j+1,visited,grid,area)
    dfs(m,n,i,j-1,visited,grid,area)
}


func maxAreaOfIsland(grid [][]int) int {
    m := len(grid)
    n := len(grid[0])
    vis := make([][]bool, m)
    ans := 0
    for ind := range vis{
        vis[ind] = make([]bool, n)
    }
            
    area := 0
    for i:=0; i<m; i++{
        for j:=0; j<n; j++{
            area = 0
            dfs(m,n,i,j,vis,grid,&area)
            fmt.Println("max area calc", area)
            ans = max(area,ans)
        }
    }
    return ans
}