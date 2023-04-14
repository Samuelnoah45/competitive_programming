class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        players.sort()
        trainers.sort()
        l = 0
        r = 0
        match = 0
        print(players , trainers)
        while l < len(players) and r < len(trainers):
            if players[l]  > trainers[r]:
                r += 1
            else:
                match +=1 
                l += 1
                r += 1
        return match