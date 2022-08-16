import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        relations = collections.defaultdict(list)  # course: courses need to take first
        for c, need in prerequisites:
            relations[c].append(need)
        status = [0] * numCourses
        order = []

        def takeClass(course):
            # Return true if it is already took
            if status[course] == 1:
                return True
            # Return false if the course is in-progress
            if status[course] == -1:
                return False
            # Otherwise, attempt to take prerequisites
            status[course] = -1  # Now it is in-progress
            for p in relations[course]:
                if not takeClass(p):
                    return False
            status[course] = 1  # Now it is good, we took all prerequisites
            order.append(course)
            return True

        for c in range(numCourses):
            # Try attend each course
            # if one course need other course, attend those as well
            if not takeClass(c):
                return []

        return order

    # Time complexity O(n)
    # Space complexity O(2n) # Saving the relationship and also the attending status
