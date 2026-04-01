/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func lowestCommonAncestor(root *TreeNode, p *TreeNode, q *TreeNode) *TreeNode {
	if root == nil{
		return root
	}
	rootVal := root.Val
	pVal := p.Val 
	qVal := q.Val
	ans := root

	if pVal <= rootVal && qVal >= rootVal || pVal >= rootVal && qVal <= rootVal{
		return ans
	}
	if pVal < rootVal && qVal < rootVal{
		ans = lowestCommonAncestor(root.Left, p, q)
	}else{
		ans = lowestCommonAncestor(root.Right, p, q)
	}
	return ans
}
