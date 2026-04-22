
func generateParenthesis(n int) []string {
    ans := make([]string, 0)
    var dfs func(int,int,string)
    dfs = func(open, close int, temp string){
        if open == n && open == close{
            ans = append(ans, temp)
            return
        }
        if open > n{
            return
        }
        if close > open{
            return
        }
        temp=temp+"("
        dfs(open+1, close, temp)    
        temp=temp[0:len(temp)-1]+")"
        dfs(open, close+1,temp)
    }
    dfs(0,0,"")
    return ans
}