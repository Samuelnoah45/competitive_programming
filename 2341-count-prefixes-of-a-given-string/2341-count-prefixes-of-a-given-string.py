class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count=0
        for word in words:
            n=len(word)
            if s[0:n]==word:
                count+=1
        return count
        