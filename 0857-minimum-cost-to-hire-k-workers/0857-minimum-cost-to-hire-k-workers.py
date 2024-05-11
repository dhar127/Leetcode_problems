class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        if K == 1:
            return min(wage)
        
        p = zip(wage, quality)
        p = sorted(p, key=lambda k:-float(k[0])/k[1])
        wage, quality = zip(*p)
        
        heap = [-q for q in quality[-(K-1):]]
        heapq.heapify(heap)
        
        min_wage = float("Inf")
        q_sum = -sum(heap)
        
        for i in reversed(range(len(wage)-K+1)):
            total_wage = wage[i] + wage[i]*q_sum/float(quality[i])
            min_wage = min(min_wage, total_wage)
            
            if quality[i] < -heap[0]:
                q_sum = q_sum + heap[0] + quality[i]
                heapq.heappop(heap)
                heapq.heappush(heap, -quality[i])
                
                
        return min_wage