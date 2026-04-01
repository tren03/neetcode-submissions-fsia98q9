/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// Brute force - every node dfs
func dfs(r *TreeNode, m int)int{
    if r == nil{
        return 0
    }
    res := 0
    if r.Val >= m{
        res = 1
    }
    res += dfs(r.Right, max(m, r.Val))
    res += dfs(r.Left, max(m, r.Val))
    return res
}
func goodNodes(root *TreeNode) int {
    if root == nil{
        return 0
    }
    return dfs(root, root.Val)

}