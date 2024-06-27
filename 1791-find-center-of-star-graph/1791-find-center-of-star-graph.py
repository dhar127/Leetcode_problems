class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        p=[]
        for i in edges:
            for j in i:
                p.append(j)
        for i in p:
            if len(edges)==p.count(i):
                return i
            