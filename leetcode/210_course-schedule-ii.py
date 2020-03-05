class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.result=[]
        self.added=set([])
        self.next_nodes=[[] for i in range(numCourses)]
        self.indegree=[0] * numCourses
        for prerequisite in prerequisites:
            self.next_nodes[prerequisite[1]].append(prerequisite[0])
            self.indegree[prerequisite[0]]+=1
        for idx in range(numCourses):
            self.tryInsert(idx)
        return self.result if len(self.result)==numCourses else []
    def tryInsert(self,idx):
        if not self.indegree[idx] and idx not in self.added:
            self.result+=[idx]
            self.added.add(idx)
            for next_idx in self.next_nodes[idx]:
                self.indegree[next_idx]-=1
                self.tryInsert(next_idx)