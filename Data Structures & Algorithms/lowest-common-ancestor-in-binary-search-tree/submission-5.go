/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func lowestCommonAncestor(root *TreeNode, p *TreeNode, q *TreeNode) *TreeNode {
	if root.Val >= p.Val && root.Val <= q.Val || root.Val <= p.Val && root.Val >=q.Val{
		return root
	}
	if p.Val < root.Val && q.Val < root.Val{
		root = lowestCommonAncestor(root.Left, p,q)
	}else{
		root = lowestCommonAncestor(root.Right, p,q)
	}
	return root
}
