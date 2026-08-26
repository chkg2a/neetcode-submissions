class Twitter:
    def __init__(self):
        self.users = defaultdict(set)
        self.following = defaultdict(set)
        self.time = 0
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        users = {userId}
        users.update(self.following[userId])

        posts = []

        for user in users:
            for time, tweetId in self.tweets[user]:
                heapq.heappush(posts, (time, tweetId))

        while len(posts) > 10:
            heapq.heappop(posts)

        posts.sort(reverse=True)

        return [tweetId for time, tweetId in posts]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)