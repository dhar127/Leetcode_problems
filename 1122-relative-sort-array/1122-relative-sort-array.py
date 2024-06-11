class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l=[]
        for i in arr2:
            f=arr1.count(i)
            for j in range(f):
                l.append(i)
        tl=[]
        for i in arr1:
            if i not in arr2:
                tl.append(i)
        tl.sort()
        for i in tl:
            l.append(i)
        return l