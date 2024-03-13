class Solution:
    def pivotInteger(self, n: int) -> int:
        l = []
        for i in range(1, n + 1):
            l.append(i)
        for i in range(len(l)):
            if sum(l[:i+1]) == sum(l[i:]):
                return l[i]
        return -1