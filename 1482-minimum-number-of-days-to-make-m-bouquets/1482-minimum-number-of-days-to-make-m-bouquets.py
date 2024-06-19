class Solution:
    def bouquetFormed(self, bloomDay, day, conFlower):
        bouquet = 0
        temp = 0
        for i in range(len(bloomDay)):
            if bloomDay[i] <= day:
                temp += 1
            else:
                bouquet += temp // conFlower
                temp = 0
        bouquet += temp // conFlower
        return bouquet
    
    def minDays(self, bloomDay, m, k):
        n = len(bloomDay)
        if m * k > n:
            return -1
        
        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            bouquet = self.bouquetFormed(bloomDay, mid, k)
            
            if bouquet >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans