class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d=sorted(d.items(),key =lambda x:x[1],reverse=True)
        x=d[0][1]
        s=0
        for i in range(len(d)):
            if d[i][1]==x:
                s+=(d[i][1])
            else:
                break
        return s
                
        