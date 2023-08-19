class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.components = n

    def find(self, v):
        if v != self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        v1_parent = self.find(v1)
        v2_parent = self.find(v2)
        if v1_parent != v2_parent:
            self.parent[v2_parent] = v1_parent
            self.components -= 1
            return True
        return False


def solution(n: int, edges: list[list[int]]) -> list[int]:
    edges = [(u, v, w, i) for i, (u, v, w) in enumerate(edges)]
    edges.sort(key=lambda x: x[2])

    min_w = 0
    uf = UnionFind(n)
    for v1, v2, w, i in edges:
        if uf.union(v1, v2):
            min_w += w

    critical = set()
    pseudo = set()
    for v1, v2, w, i in edges:
        uf = UnionFind(n)
        ignore_w = 0
        for x, y, z, j in edges:
            if i != j and uf.union(x, y):
                ignore_w += z
        if uf.components != 1 or ignore_w > min_w:
            critical.add(i)
        else:
            uf = UnionFind(n)
            force_w = w
            uf.union(v1, v2)
            for x, y, z, j in edges:
                if i != j and uf.union(x, y):
                    force_w += z
            if force_w == min_w:
                pseudo.add(i)

    return [list(critical), list(pseudo)]


test_cases = [
    {
        "n": 4,
        "edges": [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]],
        "expected": [[], [0, 1, 2, 3]],
    },
    {
        "n": 5,
        "edges": [
            [0, 1, 1],
            [1, 2, 1],
            [2, 3, 2],
            [0, 3, 2],
            [0, 4, 3],
            [3, 4, 3],
            [1, 4, 6],
        ],
        "expected": [[0, 1], [2, 3, 4, 5]],
    },
    {
        "n": 6,
        "edges": [
            [0, 1, 1],
            [1, 2, 1],
            [0, 2, 1],
            [2, 3, 4],
            [3, 4, 2],
            [3, 5, 2],
            [4, 5, 2],
        ],
        "expected": [[3], [0, 1, 2, 4, 5, 6]],
    },
]


def test_solution():
    for test_case in test_cases:
        n, edges, expected = test_case["n"], test_case["edges"], test_case["expected"]
        got = solution(n, edges)
        if got != expected:
            print(f"FAILED: test_case: {test_case}, got: {got}")


if __name__ == "__main__":
    test_solution()
