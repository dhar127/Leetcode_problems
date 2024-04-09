class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        i = 0 
        length = len(tickets)
        while tickets[k] != 0 :
            if i == length :
                i = 0 
            if tickets[i] != 0 :
                time += 1
                tickets[i] -= 1
            i += 1
        return time
