/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isSameTree(p *TreeNode, q *TreeNode) bool {
	//base conditions 
	if p == nil && q == nil{
		return true
	}
	if (p == nil && q != nil) || (p != nil && q == nil){
		return false
	}
	if p.Val != q.Val {
		return false
	}

	l := isSameTree(p.Left, q.Left)
	r := isSameTree(p.Right, q.Right)

	// operations



	return l && r
    
}
