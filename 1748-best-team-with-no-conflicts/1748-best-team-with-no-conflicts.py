class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        score_age = sorted(zip(ages,scores))
        dp = [0] * len(ages)

        for i in range(len(score_age)):
            val = float("-inf")
            for j in range(i,-1, -1):
                if score_age[i][1] >= score_age[j][1]:
                    val = max(dp[j], val)
            if val != float("-inf"):
                dp[i] = val
            dp[i] += score_age[i][1] 
        
        return max(dp)