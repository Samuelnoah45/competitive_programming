class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        info = sorted(list(zip(position, speed)) ,key=lambda x: x[0])
        ans = 1
        timeTake = [(target - x[0])/x[1] for x in info ]
        timeTake.reverse()
        monoStack = []
        l = 0
        r = 0

        while r < len(timeTake):
            if timeTake[l] >= timeTake[r]:
                r += 1
            else:
                ans += 1
                l = r
                
        return ans