class Solution:
    def longestSubarray(self, arr: List[int], l: int) -> int:
        i, j, ret = 0, 0, 0
        q1 = deque()  
        q2 = deque()  

        for j in range(len(arr)):
            
            while q1 and arr[q1[-1]] > arr[j]:
                q1.pop()
            q1.append(j)

            
            while q2 and arr[q2[-1]] < arr[j]:
                q2.pop()
            q2.append(j)

            
            while arr[q2[0]] - arr[q1[0]] > l:
                if q2[0] == i:
                    q2.popleft()
                if q1[0] == i:
                    q1.popleft()
                i += 1

            ret = max(ret, j - i + 1)

        return ret