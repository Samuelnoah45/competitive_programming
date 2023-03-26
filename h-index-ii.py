class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.reverse()
        l = -1 
        r = len(citations)

        while l + 1  < r:
            md = l + (r - l) //2

            if md + 1 > citations[md]:
                r = md
            else:
                l = md
        return r