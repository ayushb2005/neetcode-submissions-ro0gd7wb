class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashmap = defaultdict(list)

        for x,y in edges:
            hashmap[x].append(y)
            hashmap[y].append(x)
        
        seen = set()
        def dfs(node):
            if node in seen:
                return 
            seen.add(node)

            for neighbor in hashmap[node]:
                dfs(neighbor)
        count = 0 
        for i in range(n):
            if i not in seen:
                count += 1
                dfs(i)
        return count