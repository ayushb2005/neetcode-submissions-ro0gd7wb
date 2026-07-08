class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        take a max PQ with the most element then once used add it to a queue
        where (amount, time until task is available (time + n))
        '''
        hashmap = {}
        for i in tasks:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        # PQ (3, A)
        array = list(hashmap.values())
        array = [-x for x in array]
        heapq.heapify(array)
        queue = deque()

        time = 0
        while(True):
            if not array and not queue:
                return time
            time += 1
            if array:
                pop = heapq.heappop(array)
                if(pop + 1 != 0):
                    queue.append((pop+1, time + n))
            if queue:
                if(queue[0][1] == time):
                    popQueue = queue.popleft()
                    heapq.heappush(array, popQueue[0])
            
        return time
            

