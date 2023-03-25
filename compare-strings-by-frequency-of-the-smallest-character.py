import bisect
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        arr = []
        for  word in words:
            wordHash =Counter(word)
            arr.append(wordHash[min(wordHash)])
        arr.sort()

        ans = []
        for query in queries:
            queryHash = Counter(query)

            pos = bisect.bisect_right(arr, queryHash[min(queryHash)])
            ans.append(len(arr) - pos)

        return ans