/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func rec(root *TreeNode) int{
    if root == nil{
        return 0
    }
    left := rec(root.Left) + 1
    right := rec(root.Right) + 1
    return max(left,right)
}

func isBalanced(root *TreeNode) bool {
    // base condition
    if root == nil{
        return true
    }
    left := rec(root.Left)
    right := rec(root.Right)
    if math.Abs(float64(left - right)) > 1{
        return false
    }
    leftbal := isBalanced(root.Left)
    rightbal := isBalanced(root.Right)

    if !leftbal || !rightbal{
        return false
    }else{
        return true
    }
}
