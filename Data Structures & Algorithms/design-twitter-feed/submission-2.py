class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set) # userId -> set of followeeId 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 # for most recent heap

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId not in self.tweetMap:
                continue
            index = len(self.tweetMap[followeeId]) - 1
            count, tweetId = self.tweetMap[followeeId][index]
            min_heap.append([count, tweetId, followeeId, index - 1]) # where index - 1 is the next index to look at in the followers tweet list
        
        self.followMap[userId].remove(userId)
        heapq.heapify(min_heap)

        while min_heap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(min_heap, [count, tweetId, followeeId, index - 1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        

