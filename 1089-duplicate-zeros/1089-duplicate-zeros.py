class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        new=arr[:]
        i,j=0,0
        while j<len(arr):
            arr[j]=new[i]
            j+=1
            if new[i]==0:
                if j<len(arr):
                    arr[j]=new[i]
                    j+=1
            i+=1
        