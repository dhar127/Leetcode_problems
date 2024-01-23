class Solution:
    def maxLength(self, arr: List[str]) -> int:
        c, m= [''], 0
        if len(arr)==len(set(arr)):
            for s in arr:
                for w in c:
                    r = w + s
                    if len(r) != len(set(r)):
                        continue
                    c.append(r)
                    m= max(m, len(r))
        return m
        