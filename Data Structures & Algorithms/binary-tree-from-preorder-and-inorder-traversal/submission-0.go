/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func buildTree(preorder []int, inorder []int) *TreeNode {
    if len(preorder) == 0{
        return nil
    }
    rootVal := preorder[0]
    i := 0
    for ind,val := range inorder{
        if val == rootVal{
            i = ind
            break
        }
    }
    leftSub := buildTree(preorder[1:i+1], inorder[:i])
    rightSub := buildTree(preorder[i+1:], inorder[i+1:])
    return &TreeNode{Val:rootVal, Left:leftSub, Right:rightSub}
}