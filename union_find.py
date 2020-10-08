class DisjointSet:
    def __init__(self, nums):
        self.parent = {i: i for i in nums}
        self.height = {i: 0 for i in nums}
        self.count = len(nums)

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
