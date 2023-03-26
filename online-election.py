import bisect, collections

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.winners = []
        self.times = times
        Hash = defaultdict(lambda :[0, 0])
        for i in range(len(times)):
            Hash[persons[i]][0] += 1
            Hash[persons[i]][1] = times[i]
            winner = max(Hash ,key=Hash.get)

            self.winners.append((winner,times[i]))
        print(self.winners)

    def q(self, t: int) -> int:
        return self.winners[bisect.bisect(self.times, t)-1][0]