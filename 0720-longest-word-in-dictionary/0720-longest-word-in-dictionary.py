class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.val = ''           # to define the value of end node as word

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        cur.val = word     # definging the end value as whole word
    
    def bfs(self):         # as I am starting from the root itself, so bfs have only argument self for referring the root
        q = [self.root]
        res = ''
        while q:
            cur = q.pop(0)
            for child in cur.children.values():     # traversing all the nodes of cur not keys
                if child.endOfWord:                 # ONLY go to the node which is of length 1 and end of a word also
                    q.append(child)
                    if len(child.val) > len(res):   # for greater length as for lexicografical I have already sorted words 
                        res = child.val
        return res
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()        # sort in lexicografical order
        trie = Trie()       # making object of the Trie Class
        for word in words:  # adding all words to trie structre
            trie.addWord(word)
        
        return trie.bfs()   # calling the bfs function 