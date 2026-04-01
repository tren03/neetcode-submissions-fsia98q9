/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func rec(root *TreeNode, ans *int) int{
	if root == nil{
		return 0
	}
	left := rec(root.Left, ans)
	right := rec(root.Right, ans)
	*ans = max(*ans, left + right)
	return max(left, right) + 1
}
func diameterOfBinaryTree(root *TreeNode) int {
	ans := 0
	rec(root, &ans)
	return ans
}
