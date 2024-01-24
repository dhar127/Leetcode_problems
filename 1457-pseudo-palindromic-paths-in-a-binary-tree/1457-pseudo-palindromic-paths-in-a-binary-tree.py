class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        digits = [0] * 10
        return self.dfs(root, digits)

    def dfs(self, root: TreeNode, digits: list) -> int:
        if not root:
            return 0

        digits[root.val] += 1
        if not root.left and not root.right:
            cnt = self.count_odd(digits)
            digits[root.val] -= 1  
            return 1 if cnt <= 1 else 0

        left_count = self.dfs(root.left, digits)
        right_count = self.dfs(root.right, digits)

        digits[root.val] -= 1  

        return left_count + right_count

    def count_odd(self, digits: list) -> int:
        cnt = 0
        for i in range(1, 10):
            if digits[i] & 1:
                cnt += 1
        return cnt