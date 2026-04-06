class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        dp[0]=True
        words=set(wordDict)
        for i in range(1,len(s)+1):
            for word in words:
                if i-len(word)>=0:
                    if s[i-len(word):i]==word and dp[i-len(word)]:
                        dp[i]=True
        return dp[len(s)]