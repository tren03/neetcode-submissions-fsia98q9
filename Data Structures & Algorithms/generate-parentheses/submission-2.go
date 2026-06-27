func generateParenthesis(n int) []string {
    // prune search tree when we open == n
    var rec func(string, int, int)
    ans := make([]string, 0)

    rec = func(t string, open int, c int){
        if len(t) == n*2 && open == c{
            ans = append(ans, t)
            return
        }
        // include open, max open cannot be more than n
        if open != n{
            rec(t+"(", open+1, c)
        }

        // include close, if close greater than open, no valid perm exists
        if c < open{
            rec(t+")", open, c+1)
        }
    }
    rec("", 0,0)
    return ans

}
