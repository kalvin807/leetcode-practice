from collections import deque


class MyStack:
    def __init__(self):
        self.queue = deque()
        self.reverse = deque()

    def push(self, x: int) -> None:
        self.reverse.append(x)
        while self.queue:
            self.reverse.append(self.queue.popleft())
        self.queue, self.reverse = self.reverse, self.queue

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


def run_test_case(actions, value):
    result = [None for _ in range(len(value))]
    stack = None
    for i, (act, v) in enumerate(zip(actions, value)):
        if act == "MyStack":
            stack = MyStack()
        if act == "push":
            stack.push(v[0])
        if act == "pop":
            result[i] = stack.pop()
        if act == "top":
            result[i] = stack.top()
        if act == "empty":
            result[i] = stack.empty()
    return result


if __name__ == "__main__":
    cases = [
        {
            "action": ["MyStack", "push", "push", "top", "pop", "empty"],
            "value": [[], [1], [2], [], [], []],
            "expect": [None, None, None, 2, 2, False],
        }
    ]

    for c in cases:
        result = run_test_case(c["action"], c["value"])
        if result == c["expect"]:
            print("OK")
        else:
            print(f"FAIL got: {result} expect: {c['expect']}")
