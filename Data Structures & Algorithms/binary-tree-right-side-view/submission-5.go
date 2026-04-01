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
    node *TreeNode
    lev int
}
func rightSideView(root *TreeNode) []int {
    ans := make([]int, 0)
    q := make([]qnode, 0)
    
    if root == nil{
        return ans
    }
    
    q = append(q, qnode{root, 0})

    for len(q) > 0{
        cur := q[0]
        q = slices.Delete(q, 0, 1)
        level := cur.lev
        if len(ans) == level{
            ans = append(ans, cur.node.Val)
        }
        fmt.Println(cur)
        if cur.node.Right != nil{
            fmt.Println("appending non nil", cur.node.Right)
            q = append(q,qnode{cur.node.Right, level+1})
        }
        if cur.node.Left != nil{
            fmt.Println("appending non nil", cur.node.Left)
            q = append(q,qnode{cur.node.Left, level+1})
        }
    }

    return ans
}