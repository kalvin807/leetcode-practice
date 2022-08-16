import collections

# 0 = never take; -1 = in-progress, 1 = done
class Solution:
    def walk(self, course, isTook, relations):
        if isTook[course] == 1:  # already took before
            return True
        if isTook[course] == -1:  # cycle detected
            return False
        need = relations.get(course, [])
        isTook[course] = -1
        for c in need:
            if not self.walk(c, isTook, relations):
                return False
        isTook[course] = 1
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        relations = collections.defaultdict(list)

        for course, need in prerequisites:
            relations[course].append(need)

        isTook = [0] * numCourses
        for course in range(numCourses):
            if not self.walk(course, isTook, relations):
                return False
        return True

    # Time O(n)
    # Space O(n)
