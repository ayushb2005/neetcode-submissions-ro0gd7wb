class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        adjacentcy list
        DFS 
        initially n components and if i can make an edge between them
        then -1 for the amount of components
        '''
        hashMap = {}
        visitSet = set()
        connectedComponents = 0
        for i in range(n):
            hashMap[i] = []
        for n1,n2 in edges:
            hashMap[n1].append(n2)
            hashMap[n2].append(n1)
        def dfs(i):
            if i in visitSet:
                return 0
            visitSet.add(i)
            for num in hashMap[i]:
                dfs(num)
            return 1
        for i in range(n):
            connectedComponents += dfs(i)
        return connectedComponents
            