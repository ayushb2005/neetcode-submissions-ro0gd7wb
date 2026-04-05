class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        edges must be n-1
        number of nodes visited == n
        keep track of previous node, once no nodes are left to 
        continue on then return True
        '''
        if not n:
            return True
        if(len(edges) > n-1):
            return False
        elif(len(edges) < n-1):
            return False
        hashMap = {}
        for i in range(n):
            hashMap[i] = []
        for n1, n2 in edges:
            hashMap[n1].append(n2)
            hashMap[n2].append(n1)
        visitSet = set()
        def dfs(i, prev):
            if(i in visitSet):
                return False
            visitSet.add(i)
            for num in hashMap[i]:
                if(num != prev):
                    if not dfs(num,i):
                        return False
            return True
        if(dfs(0,-1) and len(visitSet) == n):
            return True
        return False
