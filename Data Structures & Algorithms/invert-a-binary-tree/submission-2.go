/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func invertTree(root *TreeNode) *TreeNode {
	if root == nil{
		return root
	}

	left := invertTree(root.Right)
	right := invertTree(root.Left)

	root.Left = left
	root.Right = right

	return root

}
