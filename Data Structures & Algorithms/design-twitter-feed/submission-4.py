class Twitter:

    def __init__(self):
        self.user_followee:dict[int,set(int)] = {}
        self.tweets:dict[int,list[int,int]] = {}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1

        if not userId in self.tweets:
            self.tweets[userId] = []

        #self.user_followee[userId].add(userId)
        self.tweets[userId].append((self.time,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        mheap = []
        followees = list(self.user_followee.get(userId,[]))
        if userId not in followees:
            followees.append(userId)

        for u in followees:

            # fetch most recent tweets
            tweets = self.tweets.get(u,[])
            if not tweets:
                continue
            recent_tweet = tweets[-1][1]
            recent_time = tweets[-1][0]
            recent_tweet_index = len(tweets) - 1
            heapq.heappush(mheap,(-recent_time, u, recent_tweet_index))
        
        while len(feed) < 10 and mheap:
            # pop the most recent
            popped = heapq.heappop(mheap)
            user = popped[1]
            tweet_index = popped[2]
            tweet_id = self.tweets[user][tweet_index]
            feed.append(tweet_id[1])

            if tweet_index != 0:
                tweet = self.tweets[user][tweet_index-1]
                recent_time = tweet[0] 
                heapq.heappush(mheap,(-recent_time,user,tweet_index-1))

        return feed



        

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.user_followee:
            self.user_followee[followerId] = set()
        self.user_followee[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_followee[followerId]:
            self.user_followee[followerId].remove(followeeId)
        
