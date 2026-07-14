class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        union find
        '''
        self.hashmap = {}
        for i in range(1, len(edges)+1):
            self.hashmap[i] = i
        
        def find(node):
            while(self.hashmap[node] != node):
                node = self.hashmap[node]
            return node

        for i in edges:
            rootu = find(i[0])
            rootv = find(i[1])

            if(rootu != rootv):
                self.hashmap[rootv] = rootu
            else:
                return i
        
