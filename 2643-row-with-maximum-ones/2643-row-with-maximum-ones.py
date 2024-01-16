class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxi=0
        c=0
        for m in mat:
            x=m.count(1)
            if x>maxi:
                maxi=x
                c=mat.index(m)
        return [c,maxi]
        