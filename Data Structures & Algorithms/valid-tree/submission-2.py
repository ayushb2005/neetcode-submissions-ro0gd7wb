class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.visit = set()
        self.hashmap = defaultdict(list)


        for i in edges:
            self.hashmap[i[0]].append(i[1])
            self.hashmap[i[1]].append(i[0])
        
        def dfs(node, prev):
            if node in self.visit:
                return False
            self.visit.add(node)
            for i in self.hashmap[node]:
                if(i != prev):
                    if not dfs(i, node):
                        return False
            return True

        if not dfs(0, -1):
            return False
        if len(self.visit) != n:
            return False
        return True
                
                


