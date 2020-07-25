class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        for j in employees:
            if j.id == id:
                src = j
        ans = src.importance
        for dep in src.subordinates:
            ans += self.getImportance(employees, dep)
        return ans