import collections

class Solution:
    def dfs(self, i):
        if self.walked[i] == -1: # Visited but unfinished
            return False
        elif self.walked[i] == 1: # Visited and finished
            return True
        else:
            self.walked[i] = -1
            for pre in self.graph[i]:
                if not self.dfs(pre):
                    return False
            self.walked[i] = 1
            self.path.append(i)
        return True
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = collections.defaultdict(list)
        # Create a graph, where the graph means a course need b course
        for course, pre in prerequisites:
            self.graph[course].append(pre)

        self.path = []
        self.walked = [0 for _ in range(numCourses)]
        # Try walk from each course
        for i in range(numCourses):
            # Walk unwalked course
            # Failed (cycle) dfs will return false, return [] 
            if not self.dfs(i):
                return []
        return self.path
