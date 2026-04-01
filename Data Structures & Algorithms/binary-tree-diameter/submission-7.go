/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
var ans int
func dfs(root *TreeNode) int{
	if root == nil{
		return 0
	}
	left := 1 + dfs(root.Left)
	right := 1 + dfs(root.Right)
	ans = max(left+right - 2, ans) // remove duplicate node, and remove 1 more for edge count
	return max(left, right)
}
func diameterOfBinaryTree(root *TreeNode) int {
	ans = 0
	dfs(root)
	return ans
}
