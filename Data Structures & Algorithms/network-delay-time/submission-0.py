class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g=defaultdict(list)
        for u,v,w in times:
            g[u].append((v,w))
        d={i:float("inf") for i in range(1,n+1)}
        h=[(0,k)]
        p={i:None for i in range(1,n+1)}
        d[k]=0
        while h:
            cost,node=heapq.heappop(h)
            for nei,w in g[node]:
                n_c=cost+w
                if n_c<d[nei]:
                    d[nei]=n_c
                    p[nei]=node
                    heapq.heappush(h,(n_c,nei))
        print(d)
        result=max(d.values())
        return -1 if result==float('inf') else result