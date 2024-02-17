class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minheap=[]
        for i in range(len(heights)-1):

            if heights[i+1]-heights[i] >0:
                heapq.heappush(minheap,(heights[i+1]-heights[i]))

            if len(minheap) > ladders:
                bricks-=heapq.heappop(minheap)
            
            if bricks < 0:
                return i

        return len(heights)-1
        