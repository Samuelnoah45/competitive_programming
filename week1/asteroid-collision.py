class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n, result, ind = len(asteroids), [], 0
        while ind < n:
            if len(result) == 0:
                result.append(asteroids[ind])
            else:
                prev, cur = result[-1], asteroids[ind]
        # case 1 and case 2 and case 3:
                if prev < 0 or cur > 0:
                    result.append(cur)
        # case 4:
                else:
                    if prev == abs(cur):
                        result.pop()
                    elif prev < abs(cur):
                        result.pop()
                        ind -= 1
            ind +=  1
        return result