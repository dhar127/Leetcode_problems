class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        p=0
        for i in range(0,n+1):
            l.append(bin(i)[2:].count('1'))
        return l