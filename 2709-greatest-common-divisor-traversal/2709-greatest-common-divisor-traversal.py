class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        mx = max(nums)
        pos = [[] for _ in range(mx + 1)]
        for i, num in enumerate(nums):
            pos[num].append(i)

        g = defaultdict(list)
        for d in range(2, mx + 1):
            seq = chain.from_iterable(pos[m] for m in range(d, mx + 1, d))
            for i, j in pairwise(seq):
                g[i].append(j)
                g[j].append(i)

        seen = [False] * len(nums)
        def dfs(v: int) -> None:
            seen[v] = True
            for u in g[v]:
                if not seen[u]:
                    dfs(u)

        dfs(0)
        return all(seen)

        