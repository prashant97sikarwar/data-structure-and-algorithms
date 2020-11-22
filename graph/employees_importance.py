class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees, id):
        for j in employees:
            if j.id == id:
                src = j
        ans = src.importance
        for dep in src.subordinates:
            ans += self.getImportance(employees, dep)
        return ans