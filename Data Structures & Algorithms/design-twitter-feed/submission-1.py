import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.follows=defaultdict(set)
        self.tweets=defaultdict(list)
        self.timeStamp=0
             
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timeStamp+=1
        self.tweets[userId].append((self.timeStamp,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        all_users={userId} | self.follows[userId]
        max_heap=[]
        result=[]
        for user in all_users:
            if self.tweets[user]:
                recent_tweet_index=len(self.tweets[user])-1
                timestamp,tweetid=self.tweets[user][recent_tweet_index]
                heapq.heappush(max_heap,(-timestamp,tweetid,user,recent_tweet_index))
        while max_heap and len(result)<10:
            timestamp,tweetid,user,recent_tweet_index=heapq.heappop(max_heap)
            result.append(tweetid)
            if recent_tweet_index>0:
                timestamp,tweetid=self.tweets[user][recent_tweet_index-1]
                heapq.heappush(max_heap,(-timestamp,tweetid,user,recent_tweet_index-1))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)