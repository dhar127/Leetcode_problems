class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        avg,num,check = sum(arr)//3,0,0
        for i in arr:
            check += i 
            if check == avg:
                num += 1
                check = 0 
        return num >= 3 and not (sum(arr))%3