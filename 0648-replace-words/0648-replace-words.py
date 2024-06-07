class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def shortest_prefix(self, word):
        node = self.root
        prefix = ""
        for char in word:
            if char in node.children:
                prefix += char
                if node.children[char].is_end_of_word:
                    return prefix
                node = node.children[char]
            else:
                return word
        return word

class Solution:
    def replaceWords(self, dictionary, sentence):
        trie = Trie()
        for root in dictionary:
            trie.insert(root)

        words = sentence.split()
        replaced_sentence = []
        for word in words:
            replaced_sentence.append(trie.shortest_prefix(word))

        return " ".join(replaced_sentence)

