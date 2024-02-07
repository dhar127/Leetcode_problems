class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
        optimized_string = ''.join(char * count for char, count in sorted_char_count)
        return optimized_string
        