import math 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest=[]
        distance=float("inf")
        points.sort(key=lambda x:x[0]*x[0]+x[1]*x[1])
        print(points)

        for point in  points:
            isClosest=point[0]*point[0]+point[1]*point[1]
            if isClosest<distance:
                isClosest=distance
                closest.append([point[0],point[1]])
                if len(closest)==k:
                    break
        print(closest)
        return closest



