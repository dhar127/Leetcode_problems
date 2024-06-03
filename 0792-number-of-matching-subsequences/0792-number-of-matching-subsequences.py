class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_subsequence(word: str, index_map: dict) -> bool:
            prev_index = -1
            for char in word:
                if char not in index_map:
                    return False
                positions = index_map[char]
                # Find the smallest index greater than prev_index
                i = bisect.bisect_left(positions, prev_index + 1)
                if i == len(positions):
                    return False
                prev_index = positions[i]
            return True

        # Preprocessing: create index mapping for characters in s
        index_map = defaultdict(list)
        for i, char in enumerate(s):
            index_map[char].append(i)

        # Check each word if it's a subsequence of s
        count = 0
        for word in words:
            if is_subsequence(word, index_map):
                count += 1
        return count
