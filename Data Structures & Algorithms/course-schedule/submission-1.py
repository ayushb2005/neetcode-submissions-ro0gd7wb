class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        keep a seen set of nodes that I have already seen
        use a DFS, and go visit nodes 1 by 1, from the hashmap
        visit the 1st in the list then visit that and see if there are
        any nodes that i can keep going until i hit []
        then i marked that as visited

        if node is prove safe, meaning it is [] then no need to visit it 
        even if two nodes point to it
        ex. 1->3 and 1->4 and 3->4 but 4 is []
        can only remove from the array in the hm if proven safe
        '''
        visitSet = set()
        hashMap = {}
        stack = []

        for lst in prerequisites:
            if(lst[0] in hashMap):
                hashMap[lst[0]].append(lst[1])
            else:
                hashMap[lst[0]] = [lst[1]]
        for i in range(numCourses):
            if i not in hashMap:
                hashMap[i] = []
        def dfs(crs):
            if crs in visitSet:
                return False
            if hashMap[crs] == []:
                return True
            visitSet.add(crs)
            for cr in hashMap[crs]:
                if not dfs(cr): return False
            visitSet.remove(crs)
            hashMap[crs] = []
            return True
        for i in range(numCourses):
            if not dfs(i): return False
        return True
        # for i in range(numCourses-1):
        #     #run dfs on i
        #     stack = []
        #     stack.append(i)
        #     while(stack):
        #         value = stack.pop()
        #         if(not hashMap[value]):
        #             seen.add(value)
        #         else:
        #             for num in hashMap[value]:
        #                 if num in seen:
        #                     return False
        #                 else:
        #                     stack.append(num)
        # return True



