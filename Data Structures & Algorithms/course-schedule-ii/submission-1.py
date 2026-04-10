class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        igraph=defaultdict(list)
        indegree={node:0 for node in range(numCourses)}

        for u,v in prerequisites:
            graph[u].append(v)
        
        for u,v in prerequisites:
            igraph[v].append(u)
        
        for node in igraph:
            for neighbor in igraph[node]:
                indegree[neighbor]+=1
        v=set()
        for i in indegree:
            if i not in v and indegree[i]==0:
                v.add(i)
        
        #Khans
        kq=deque()
        for node in indegree:
            if indegree[node]==0:
                kq.append(node)
        kv=[]
        while kq:
            print("Khans queue: ",kq)
            node=kq.popleft()
            kv.append(node)
            for neighbors in igraph[node]:
                indegree[neighbors]-=1
                if indegree[neighbors]==0:
                    kq.append(neighbors)
        
        if len(kv)!=numCourses:
            kv=[]

        #BFS
        q=deque()

        for node in graph:
            if graph[node]:
                q.append(node)
        
        while q:
            node=q.popleft()
            v.add(node)
            for neighbors in graph[node]:
                if neighbors not in v:
                    q.append(neighbors)
        

        result=[]
        if not prerequisites:
            return kv[::-1]
        else:
            for node in kv:
                if node in v:
                    result.append(node)
            return result