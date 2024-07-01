class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        g=0
        for i in range(len(arr)-2):
            h=0
            for j in range(i,i+3):
                if arr[j]%2!=0:
                    h+=1
            if h==3:
                return True
        return False
                