class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        hashmap = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                star = word[:j] + "*" + word[j+1:]
                hashmap[star].append(word)

        queue = deque([beginWord])
        seenSet = {beginWord}
        counter = 1

        while(queue):
            length = len(queue)
            for _ in range(length):
                pop = queue.popleft()
                if(pop == endWord):
                    return counter
                for j in range(len(pop)):
                    star = pop[:j] + "*" + pop[j+1:]
                    for i in hashmap[star]:
                        if i not in seenSet:
                            seenSet.add(i)
                            queue.append(i)
                print(queue)
            counter += 1
        return 0



        
        