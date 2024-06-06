from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = "balon"
        char_count = Counter(text)
        min_count = float('inf') 
        for char in balloon:
            if char == 'l' or char == 'o':
                min_count = min(min_count, char_count[char] // 2)
            else:
                min_count = min(min_count, char_count[char])

        return min_count