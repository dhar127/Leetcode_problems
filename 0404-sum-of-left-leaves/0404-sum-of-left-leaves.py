# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        s=0
        if root.left:
            if not root.left.left and not root.left.right:
                s+=root.left.val
            else:
                s+=self.sumOfLeftLeaves(root.left)
        s+=self.sumOfLeftLeaves(root.right)
        return s