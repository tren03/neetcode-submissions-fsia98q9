/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func maxDepth(root *TreeNode) int {
	if root == nil{
		return 0
	}
	
	left := maxDepth(root.Left) 
	right := maxDepth(root.Right) 

	return max(left+1, right+1)
    
}
