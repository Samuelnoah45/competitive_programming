class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()
        l = 0
        r = len(skill) - 1
        avg = skill[l] + skill[r]
        ans = 0
        while l < r:
            if (skill[l] + skill[r]) == avg:
                ans += skill[l] * skill[r]
                r -= 1
                l += 1
            else:
                return -1

        return ans