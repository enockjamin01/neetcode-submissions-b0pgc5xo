class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class Union:
            def __init__(self,n):
                self.makeset(n)
            def makeset(self,n):
                self.parent=[x for x in range(n+1)]
                self.size=[1 for x in self.parent]
            def find(self,x):
                if self.parent[x]!=x:
                    self.parent[x]=self.find(self.parent[x])
                return self.parent[x]
            def union(self,u,v):
                x,y=self.find(u),self.find(v)
                if x==y:
                    return False
                if self.size[x]<self.size[y]:
                    self.parent[x]=y
                    self.size[y]+=self.size[x]
                else:
                    self.parent[y]=x
                    self.size[x]+=self.size[y]
                return True
        obj=Union(len(edges))
        for edge in edges:
            flag=obj.union(edge[0],edge[1])
            if not flag:
                return edge