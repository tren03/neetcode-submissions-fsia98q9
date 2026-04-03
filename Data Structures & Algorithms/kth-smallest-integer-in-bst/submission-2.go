/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */


func kthSmallest(root *TreeNode, k int) int {
    ans := 0
    ansFound := false
    var in func(*TreeNode) 
    in = func(r *TreeNode){
        if r == nil || ansFound == true{
            return
        }
        in(r.Left)
        k = k - 1
        if k == 0{
            ans = r.Val
            ansFound = true
            return
        }
        in(r.Right)
    }
    in(root)
    return ans
}