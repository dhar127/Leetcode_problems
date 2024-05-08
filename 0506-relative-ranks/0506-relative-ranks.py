class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s=sorted(score,reverse=True)
        l=[]
        for i in range(len(s)):
            if i==0:
                l.append([s[i],"Gold Medal"])
            elif i==1:
                l.append([s[i],"Silver Medal"])
            elif i==2:
                l.append([s[i],"Bronze Medal"])
            else:
                l.append([s[i],i+1])
        q=[]
        for i in score:
            for j in range(len(l)):
                if l[j][0]==i:
                    q.append(str(l[j][1]))
        return q