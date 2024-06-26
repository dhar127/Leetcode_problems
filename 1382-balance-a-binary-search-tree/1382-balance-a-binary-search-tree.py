# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def in_order(node):
            if not node:
                return []
            return in_order(node.left) + [node.val] + in_order(node.right)
        
        sorted_values = in_order(root)
        def balanced(values):
            if not values:
                return None
            mid = len(values) // 2
            root = TreeNode(values[mid])
            root.left = balanced(values[:mid])
            root.right = balanced(values[mid+1:])
            return root
        
        return balanced(sorted_values)