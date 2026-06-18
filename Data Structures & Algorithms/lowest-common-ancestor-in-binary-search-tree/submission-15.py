# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = [root.val]

        def heigth(root):
            if (p is root) or (q is root):
                return  

            ans[0] = root

            if root.val < p.val and root.val < q.val:
                return heigth(root.right)
            elif root.val > p.val and root.val > q.val:
                return heigth(root.left)
            else:
                return

        heigth(root)
        return ans[0]

        