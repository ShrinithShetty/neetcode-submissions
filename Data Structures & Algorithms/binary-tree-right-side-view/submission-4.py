# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()
        q.append(root)
        ans = []

        while q:
            rightside = None
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node:
                    rightside = node.val
                    q.append(node.left)
                    q.append(node.right)
            if rightside:
                ans.append(rightside)

        return ans
        
        