class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        q=collections.Counter([m[1] for m in matches])
        p=list(set([g for h in matches for g in h]))
        k=[[],[]]
        for i in p:
            if q[i]==0:
                k[0].append(i)
            elif q[i]==1:
                k[1].append(i)
        k[0]=sorted(k[0])
        k[1]=sorted(k[1])
        return k
        