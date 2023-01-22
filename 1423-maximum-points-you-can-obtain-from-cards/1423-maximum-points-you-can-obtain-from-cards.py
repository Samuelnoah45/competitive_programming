class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = len(cardPoints)-k

        cal = sum(cardPoints[right:])
        ans = cal
        while right < len(cardPoints):
            cal += (cardPoints[left]-cardPoints[right])
            ans = max(ans,cal)
            right += 1
            left += 1

        return ans

        