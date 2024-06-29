from typing import List
from collections import defaultdict, deque

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        v_edges = [set() for i in range(n)]
        for u, v in edges:
            v_edges[v].add(u)
        
        @cache
        def dfs(v):
            children = set()
            for v2 in v_edges[v]:
                children.add(v2)
                children |= dfs(v2)
            return children
        
        ans = [dfs(v) for v in range(n)]
        return [sorted(list(i)) for i in ans] 