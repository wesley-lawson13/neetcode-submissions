class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        heap = []

        self.follow_map[userId].add(userId)
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                time, tweetId = self.tweet_map[followeeId][-1]
                index = len(self.tweet_map[followeeId]) - 1
                heap.append((time, tweetId, followeeId, index - 1))

        self.follow_map[userId].remove(userId)

        heapq.heapify(heap)
        ret = []
        while heap and len(ret) < 10:
            _, tweetId, followeeId, index = heapq.heappop(heap)
            ret.append(tweetId)

            if index >= 0:
                time, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(heap, (time, tweetId, followeeId, index - 1))

        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follow_map[followerId]:
            return
        self.follow_map[followerId].remove(followeeId)
        
