class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.visit = set()
        self.hashmap = defaultdict(list)
        for i in prerequisites:
            self.hashmap[i[0]].append(i[1])

        def dfs(node):
            if node in self.visit:
                return False
            self.visit.add(node)
            if self.hashmap[node]:
                for i in self.hashmap[node]:
                    if not dfs(i):
                        return False
                self.hashmap[node] = []
            self.visit.remove(node)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        
