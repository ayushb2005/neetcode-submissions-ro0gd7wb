class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.visit = set()
        self.hashmap = defaultdict(list)
        self.array = []
        self.processed = set()
        for i in prerequisites:
            self.hashmap[i[0]].append(i[1])
        print(self.hashmap)
        def dfs(node):
            if node in self.visit:
                return False
            self.visit.add(node)
            if self.hashmap[node]:
                for i in self.hashmap[node]:
                    if not dfs(i):
                        return False
                self.hashmap[node] = []
            if node not in self.processed:
                self.array.append(node)
                self.processed.add(node)
            self.visit.remove(node)
            return True
        for i in range(numCourses):
            # if i in self.processed:
            #     continue
            if not dfs(i):
                return []
        return self.array
