class Twitter:

    def __init__(self):
        self.userToFollowing = {}
        self.userToTweets = {}
        self.postCount = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userToTweets:
            self.userToTweets[userId] = deque([])
        self.userToTweets[userId].append((self.postCount, tweetId))
        if len(self.userToTweets[userId]) > 10:
            self.userToTweets[userId].popleft()
        
        self.postCount += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        if userId not in self.userToFollowing:
            self.userToFollowing[userId] = set([userId])

        heap = []
        for followingId in self.userToFollowing[userId]:
            if followingId in self.userToTweets:
                index = len(self.userToTweets[followingId]) - 1
                count, tweetId = self.userToTweets[followingId][index]
                heapq.heappush_max(heap, (count, followingId, tweetId, index))
        
        while heap and len(feed) < 10:
            count, uId, tweetId, index = heapq.heappop_max(heap)
            feed.append(tweetId)
            if index > 0:
                n_count, n_tweetId = self.userToTweets[uId][index-1]
                heapq.heappush_max(heap, (n_count, uId, n_tweetId, index-1))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userToFollowing:
            self.userToFollowing[followerId] = set([followerId])
        self.userToFollowing[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.userToFollowing[followerId]:
            return
        self.userToFollowing[followerId].remove(followeeId)