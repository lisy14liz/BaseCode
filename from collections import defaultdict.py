from collections import defaultdict
class DisjointSet:
    def __init__(self, n,m):
        self.parent = {(i,j): (i,j) for i in n for j in m}
        self.height = {(i,j): 0 for i in n for j in m}
        self.count = n*m

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return xRoot
        (lower, higher) = (
            xRoot, yRoot) if self.height[xRoot] < self.height[yRoot] else (yRoot, xRoot)
        self.parent[lower] = higher
        if self.height[higher] == self.height[lower]:
            self.height[higher] += 1
        self.count -= 1
        return higher
def inp(type=int):
    return map(type,input().split())
N,M=inp()
A=[[] for i in range(N)]
for i in range(N):
    A[i]=list(inp())
djs=DisjointSet(N,M)
def valid(x,y):
    if x<len(A) and y<len(A[0]) and x>=0 and y>=0:
        return True
    return False
for i in range(N):
    for j in range(M):
        for di,dj in [(1,0),(0,1)]:
            if valid(i+di,j+dj) and A[i][j]==A[i+di][j+dj]==1:
                djs.union((i+di,j+dj),(i,j))
 areas= defaultdict(int)       
for i in range(N):
    for j in range(M):
        if A[i+di][j+dj]==1:
             areas[djs.find((i,j))]+=1
res=0
for i in range(N):
    for j in range(M):
        if A[i][j]==0:
            neis=set()
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                if valid(i+di,j+dj) and A[i+di][j+dj]==1:
                    neis.add(djs.find((i+di,j+dj)))
            if len(neis)>=2:
                tmp_res=0
                for area in neis:
                    tmp_res+=areas[area]
                if len(areas)>len(neis):
                    tmp_res+=1
                res=max(res,tmp_res)
return res
            