import bisect, collections

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        counter, current_leader = [0] * len(persons), 0
        self.winners = [-1] * len(times)
        self.times = times
        for idx, person in enumerate(persons):
            counter[person] += 1
            if counter[person] >= counter[current_leader]:
                current_leader = person
            self.winners[idx] = current_leader

    def q(self, t: int) -> int:
        return self.winners[bisect.bisect(self.times, t)-1]