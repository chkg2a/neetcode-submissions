class Twitter:

    def __init__(self):
        self.users = defaultdict(list)
        self.following = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].append(tweetId)

    def getNewsFeed(self, userId: int) -> list[int]:
        users = set()
        users.add(userId)
        for i in self.following[userId]:
            users.add(i)
        posts = []
        for user in users:
            for post in self.users[user]:
                heapq.heappush(posts,-post)
        while len(posts) > 10:
            heapq.heappop(posts)
        for i in range(len(posts)):
            posts[i] = -posts[i]
        return sorted(posts)

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
