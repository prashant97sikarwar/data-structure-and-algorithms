class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i in range(len(paths)):
            graph[paths[i][0]].append(paths[i][1])
            graph[paths[i][1]].append(paths[i][0])
        arr = [None] * N
        for i in range(1,N+1):
            color = set([1,2,3,4])
            for node in graph[i]:
                if arr[node-1] in color:
                    color.discard(arr[node-1])
            arr[i-1] = color.pop()
        return arr
            