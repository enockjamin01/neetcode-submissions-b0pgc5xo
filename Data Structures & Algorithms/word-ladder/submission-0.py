class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        distance={word:-1 for word in wordList}
        parent={word:None for word in wordList}
        distance[beginWord]=1
        q=deque()
        q.append(beginWord)
        g=defaultdict(list)
        for word in wordList:
            for other in wordList:
                diff=0
                for i in range(len(word)):
                    if word[i]!=other[i]:
                        diff+=1
                if diff==1:
                    g[word].append(other)
        while q:
            word=q.popleft()
            for nei in g[word]:
                if distance[nei]==-1:
                    distance[nei]=distance[word]+1
                    parent[nei]=word
                    q.append(nei)
        if distance[endWord]==-1:
            return 0
        else:
            # target=endWord
            # path=[target]
            # while target:
            #     path.append(parent[target])
            #     target=parent[target]
            # print(path[::-1])
            return distance[endWord]