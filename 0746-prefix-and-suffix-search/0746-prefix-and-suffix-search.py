class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = {}
        for idx, word in enumerate(words):
            for i in range(len(word)):
                self.add_word(word[i:] + '#' + word, idx)
    
    def add_word(self, word, idx):
        cur = self.trie
        for ch in word:
            cur.setdefault(ch, {})
            cur = cur[ch]
            cur[True] = idx

    def f(self, prefix: str, suffix: str) -> int:
        node = self.trie
        for ch in suffix + '#' + prefix:
            if ch not in node: return -1
            node = node[ch]
        return node[True]
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)