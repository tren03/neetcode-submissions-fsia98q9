/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func diameterOfBinaryTree(root *TreeNode) int {
	ans := 0
	var rec func(*TreeNode)int
	rec = func(root *TreeNode)int{
		if root == nil{
			return 0
		}
		left := rec(root.Left)
		right := rec(root.Right)
		ans = max(ans, left+right)
		return max(left,right) + 1
	}
	rec(root)
	return ans
    
}
