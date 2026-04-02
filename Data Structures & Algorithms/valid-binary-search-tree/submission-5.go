/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */


func dfs(root *TreeNode, small, big int) bool{
    if root == nil{
        return true
    }
    if root.Val <= small || root.Val >= big{
        return false
    }

    l := dfs(root.Left, small, min(big, root.Val)) // in left, max changes, so all values are below max limit
    r := dfs(root.Right, max(small, root.Val), big ) // in right, min changes, so all values are greater than min limit

    return l && r
}



func isValidBST(root *TreeNode) bool {
    return dfs(root, math.MinInt , math.MaxInt) // min max limit of each node
}