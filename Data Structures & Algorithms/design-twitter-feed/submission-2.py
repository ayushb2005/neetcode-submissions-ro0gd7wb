class Twitter:

    def __init__(self):
        self.followMap = {}
        self.tweetMap = {}
        self.count = 0 
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweetMap:
            self.tweetMap[userId].append((self.count, tweetId))
        else:
            self.tweetMap[userId] = [(self.count, tweetId)]
        self.count -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        array = []
        if userId not in self.followMap and userId not in self.tweetMap:
            return []
        if userId not in self.followMap:
            for i in self.tweetMap[userId]:
                heapq.heappush(array, i)
            counter = 10
            returnArray = []
            for i in range(len(array)):
                if(i == counter):
                    return returnArray
                pop = heapq.heappop(array)
                returnArray.append(pop[1])
            return returnArray
        else:
            for i in self.followMap[userId]:
                if i not in self.tweetMap:
                    continue
                for j in self.tweetMap[i]:
                    heapq.heappush(array, j)
            returnArray = []
            counter = 10
            for i in range(len(array)):
                if i == counter:
                    return returnArray
                pop = heapq.heappop(array)
                returnArray.append(pop[1])
            return returnArray
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].add(followeeId)
        else:
            self.followMap[followerId] = {followeeId}
        self.followMap[followerId].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if(followerId == followeeId):
            return
        if followeeId not in self.followMap[followerId]:
            return 
        self.followMap[followerId].remove(followeeId)
