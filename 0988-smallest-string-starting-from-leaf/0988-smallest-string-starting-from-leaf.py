# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        def dfs(node, path, result):
            if not node:
                return
            path = chr(node.val + ord('a')) + path
            if not node.left and not node.right: 
                result.append(path)
                return
            dfs(node.left, path, result)
            dfs(node.right, path, result)

        result = []
        dfs(root, "", result)
        return min(result)