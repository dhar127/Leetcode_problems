from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        freq_map = Counter(arr)
        freq_list = sorted(freq_map.items(), key=lambda x: x[1])

        unique_count = len(freq_list)
        for num, count in freq_list:
            if k >= count:
                k -= count
                unique_count -= 1
            else:
                break

        return unique_count
