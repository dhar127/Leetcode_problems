from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Build adjacency list representing the tree
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        # Initialize arrays to store the sum of distances and number of nodes in subtree
        sum_dist = [0] * n
        count = [0] * n
        
        # Define DFS helper function
        def dfs(node, parent):
            nonlocal sum_dist, count
            
            # Count the current node
            count[node] = 1
            
            # Traverse children
            for child in adj_list[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    sum_dist[node] += sum_dist[child] + count[child]
        
        # Perform DFS from node 0
        dfs(0, -1)
        
        # Define second DFS helper function to calculate distances
        def dfs_distances(node, parent):
            nonlocal sum_dist, count
            
            # For the current node, add distances from its parent
            if parent != -1:
                sum_dist[node] = sum_dist[parent] - count[node] + (n - count[node])
            
            # Traverse children
            for child in adj_list[node]:
                if child != parent:
                    dfs_distances(child, node)
        
        # Perform second DFS to calculate distances
        dfs_distances(0, -1)
        
        return sum_dist
