from collections import deque

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]  # If there is only one node, it's the root of MHT
        adjacency_list = [[] for _ in range(n)]
        degrees = [0] * n
        
        # Build adjacency list and calculate degrees of each node
        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)
            degrees[a] += 1
            degrees[b] += 1
        
        # Initialize queue with leaf nodes (degree == 1)
        leaves = deque([i for i in range(n) if degrees[i] == 1])
        
        while n > 2:
            # Process current level of leaf nodes
            current_level_size = len(leaves)
            n -= current_level_size
            for _ in range(current_level_size):
                leaf = leaves.popleft()
                for neighbor in adjacency_list[leaf]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        leaves.append(neighbor)
        
        # Remaining nodes in the queue are potential MHT roots
        return list(leaves)
