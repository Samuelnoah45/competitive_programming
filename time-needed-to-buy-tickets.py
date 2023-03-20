class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        idx = 0
        ans = 0 
        
        while True:   
            if tickets[idx%len(tickets)] != 0:
                tickets[idx%len(tickets)] -= 1
                ans += 1
            if idx%len(tickets) == k and tickets[k]== 0:
                break
            idx += 1
        return ans