class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashmap = defaultdict(list)

        for i,j in edges:
            hashmap[i].append(j)
            hashmap[j].append(i)
        
        seenSet = set()
        def dfs(node):
            if node in seenSet:
                return 
            seenSet.add(node)
            for i in hashmap[node]:
                dfs(i)
            return 
        count = 0
        for i in range(n):
            if i not in seenSet:
                count += 1
                dfs(i)
        return count    