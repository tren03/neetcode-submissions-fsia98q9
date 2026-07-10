/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func levelOrder(root *TreeNode) [][]int {
	ans := make([][]int, 0)
	var dfs func(*TreeNode,int)
	dfs = func(r *TreeNode, i int){
		if r == nil{
			return
		}
	if i >= len(ans){
		ans = append(ans, []int{})
	}

	ans[i] = append(ans[i], r.Val)
	dfs(r.Left, i+1)
	dfs(r.Right, i+1)
	}
	dfs(root,0)
	return ans
}
