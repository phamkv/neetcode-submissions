class Twitter:

    def __init__(self):
        self.userToFollowing = {}
        self.userToTweets = {}
        self.postCount = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userToFollowing:
            self.userToFollowing[userId] = set([userId])
        if userId not in self.userToTweets:
            self.userToTweets[userId] = []
        self.userToTweets[userId].append((self.postCount, tweetId))
        self.postCount += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        if userId not in self.userToFollowing:
            self.userToFollowing[userId] = set([userId])
        for following in self.userToFollowing[userId]:
            if following not in self.userToTweets:
                continue
            for tweet in self.userToTweets[following]:
                heapq.heappush(feed, tweet)
                if len(feed) > 10:
                    heapq.heappop(feed)
        feed.sort(key=lambda x: x[0], reverse=True)
        return [tweet[1] for tweet in feed]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userToFollowing:
            self.userToFollowing[followerId] = set([followerId])
        self.userToFollowing[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userToFollowing or followerId == followeeId or followeeId not in self.userToFollowing[followerId]:
            return
        self.userToFollowing[followerId].remove(followeeId)