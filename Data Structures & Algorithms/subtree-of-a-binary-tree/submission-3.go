/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func eq(p *TreeNode, q *TreeNode) bool{
	if p == nil && q == nil{
		return true
	}
	if p == nil && q != nil || q == nil && p != nil{
		return false
	}
	if p.Val != q.Val{
		return false
	}

	left := eq(p.Left, q.Left)
	right := eq(p.Right, q.Right)

	return left && right
}

func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
	if root == nil{
		return false
	}
	check := eq(root, subRoot)
	if check == true{ // This means we found a valid subroot
		return true
	}
	l := isSubtree(root.Left, subRoot)
	r := isSubtree(root.Right, subRoot)
	return l || r
}












