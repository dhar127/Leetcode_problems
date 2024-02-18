class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        arr = []
        for i in range(n):
            heapq.heappush(arr, (0, i)) # (endTime, roomID)
        
        cnt = collections.Counter()
        meetings.sort() # sort based on start time
        
        for i in range(len(meetings)):
            s, e = meetings[i]
            
            # free finished rooms such that low-index room can be selected first
            while arr[0][0] < s:
                curTime, idx = heapq.heappop(arr)
                heapq.heappush(arr, (s, idx))
            
            curTime, idx = heapq.heappop(arr)
            heapq.heappush(arr, (max(curTime, s) + e - s, idx))
            cnt[idx] += 1
        
        maxV = 0
        for i in range(n):
            if cnt[i] > maxV:
                res = i
                maxV = cnt[i]
        return res
        