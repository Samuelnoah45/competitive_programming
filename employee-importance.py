"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        Hash = {}
        for emp in employees:
            Hash[emp.id] = {
                "imp":emp.importance,
                "sub": emp.subordinates
            }
        ans = 0
        def dfs(emp):
            nonlocal ans
            ans +=Hash[emp]["imp"]
            for sub in Hash[emp]["sub"]:
                dfs(sub)

        for key in Hash:
            if key == id:
                dfs(key)

        return ans