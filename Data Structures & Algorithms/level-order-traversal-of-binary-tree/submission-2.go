/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
import "slices"
type qnode struct{
    root *TreeNode
    level int
}
func levelOrder(root *TreeNode) [][]int {
    q := make([]qnode, 0)
    ans := make([][]int, 0)    
    
    if root == nil{
      return ans  
    }
    q = append(q, qnode{root, 0})
    for len(q) != 0{
        v := q[len(q)-1]
        q = slices.Delete(q, len(q)-1, len(q))

        if len(ans) == v.level{
            ans = append(ans, []int{})
        }

        ans[v.level] = append(ans[v.level], v.root.Val)
        // push children to que
        if v.root.Right != nil{
            q = append(q, qnode{v.root.Right, v.level + 1})
        }
        if v.root.Left != nil{
            q = append(q, qnode{v.root.Left, v.level + 1})
        }
    }
    return ans
    
    
    
}