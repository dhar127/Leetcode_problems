class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        l=[]
        f=s.split(":")
        for i in range(ord(f[0][0]),ord(f[1][0])+1):
            for j in range(int(f[0][1]),int(f[1][1])+1):
                l.append(chr(i)+str(j))
        return l