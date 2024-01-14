class Solution:
    def pos(self,weight,mid):
        d,l=1,0
        for i in range(len(weight)):
            if weight[i]+l>mid:
                d+=1
                l=weight[i]
            else:
                l+=weight[i]
        return d
                
        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        h=sum(weights)
        while l<=h:
            m=(l+h)//2
            nod=self.pos(weights,m)
            if nod<=days:
                h=m-1
            else:
                l=m+1
        return l
        