class Node:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.current = None
        
    def add(self, url):
        node = Node(url)
        if self.current:
            node.prev = self.current
            self.current.next = node
            self.current = node
        else:
            self.current = node
    
    def goBack(self, n):
        node = self.current
        while n > 0 and node.prev:
            node = node.prev
            n -= 1
        self.current = node
        return node.url
    
    def goForward(self, n):
        node = self.current
        while n > 0 and node.next:
            node = node.next
            n -= 1
        self.current = node
        return node.url
        
    

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = DLL()
        self.visit(homepage)

    def visit(self, url: str) -> None:
        self.history.add(url)

    def back(self, steps: int) -> str:
        return self.history.goBack(steps)

    def forward(self, steps: int) -> str:
        return self.history.goForward(steps)


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
