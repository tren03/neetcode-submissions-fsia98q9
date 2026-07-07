/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isBalanced(root *TreeNode) bool {
	ans := true
	var rec func(*TreeNode)int
	rec = func(root *TreeNode) int{
		if ans == false{
			return 0
		}
		if root == nil{
			return 0
		}
		left := rec(root.Left)
		right := rec(root.Right)
		if math.Abs(float64(left - right)) > 1{
			ans = false
		}
		return max(left, right) + 1
	}
	rec(root)
	return ans
}
