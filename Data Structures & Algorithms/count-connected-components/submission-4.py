class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.connected = 0
        self.hashmap = {}
        self.seen = set()

        for edge in edges:
            if(edge[0] in self.hashmap):
                self.hashmap[edge[0]].append(edge[1])
            else:
                self.hashmap[edge[0]] = [edge[1]]
            if(edge[1] in self.hashmap):
                self.hashmap[edge[1]].append(edge[0])
            else:
                self.hashmap[edge[1]] = [edge[0]]
                
        print(self.hashmap)
        def dfs(node):
            self.seen.add(node)
            if node not in self.hashmap:
                return 
            for value in self.hashmap[node]:
                if value not in self.seen:
                    dfs(value)
        
        for i in range(n):
            if i not in self.seen:
                self.connected += 1
                dfs(i)
        return self.connected 
            
            