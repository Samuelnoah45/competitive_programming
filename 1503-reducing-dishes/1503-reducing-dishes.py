class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        result, current, ps = 0, 0, 0
        n = len(satisfaction)
        for i in range(n):
            current += ps + satisfaction[i]
            ps += satisfaction[i]
            result = max(result, current)
        return result