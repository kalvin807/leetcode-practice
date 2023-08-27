from collections import defaultdict, deque
from typing import List


class Solution:
    def topoSort(self, items, graph, indegree):
        queue = deque()
        for item in items:
            if indegree[item] == 0:
                queue.append(item)

        sorted_items = []
        while queue:
            item = queue.popleft()
            sorted_items.append(item)

            for next_item in graph[item]:
                indegree[next_item] -= 1
                if indegree[next_item] == 0:
                    queue.append(next_item)

        return sorted_items

    def sortItems(
        self, n: int, m: int, group: List[int], beforeItems: List[List[int]]
    ) -> List[int]:
        group_items = defaultdict(list)
        groupId = m
        for i in range(n):
            if group[i] == -1:
                group[i] = groupId
                groupId += 1

            group_items[group[i]].append(i)

        item_graph = defaultdict(list)
        item_indegree = defaultdict(int)

        for v, u_list in enumerate(beforeItems):
            for u in u_list:
                if group[u] == group[v]:
                    item_graph[u].append(v)
                    item_indegree[v] += 1

        sorted_group_items = {}

        for groupId in group_items:
            sorted_items = self.topoSort(
                group_items[groupId], item_graph, item_indegree
            )

            if len(sorted_items) != len(group_items[groupId]):
                return []

            sorted_group_items[groupId] = sorted_items

        group_graph = defaultdict(list)
        group_indegree = defaultdict(int)

        for v, u_list in enumerate(beforeItems):
            for u in u_list:
                if group[u] != group[v]:
                    group_graph[group[u]].append(group[v])
                    group_indegree[group[v]] += 1

        groups = set(group)

        sorted_groups = self.topoSort(groups, group_graph, group_indegree)

        if len(groups) != len(sorted_groups):
            return []

        ans = []

        for groupId in sorted_groups:
            ans.extend(sorted_group_items[groupId])

        return ans

    def test(self):
        tt = [
            {
                "n": 8,
                "m": 2,
                "group": [-1, -1, 1, 0, 0, 1, 0, -1],
                "beforeItems": [[], [6], [5], [6], [3, 6], [], [], []],
                "expected": [6, 3, 4, 1, 5, 2, 0, 7],
            },
            {
                "n": 8,
                "m": 2,
                "group": [-1, -1, 1, 0, 0, 1, 0, -1],
                "beforeItems": [[], [6], [5], [6], [3], [], [4], []],
                "expected": [],
            },
        ]

        for t in tt:
            result = self.sortItems(t["n"], t["m"], t["group"], t["beforeItems"])
            if result != t["expected"]:
                print("FAIL")
                print("result: {}".format(result))
                print("expected: {}".format(t["expected"]))
            else:
                print("SUCCESS")


if __name__ == "__main__":
    Solution().test()
