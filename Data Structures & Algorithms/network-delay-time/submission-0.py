class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # node k what we will send signal from 

        hashmap = defaultdict(list)
        for i in times:
            hashmap[i[0]].append((i[1], i[2]))
        print(hashmap)
        seenSet = set()
        storeMap = {}


        def dfs(node, count):
            if node in storeMap and count >= storeMap[node]:
                return 
            
            storeMap[node] = count

            for neighbor, time in hashmap[node]:
                dfs(neighbor, count + time)
        dfs(k, 0)
        print(storeMap)
        if len(storeMap) != n:
            return -1
        return max(storeMap.values())
        
