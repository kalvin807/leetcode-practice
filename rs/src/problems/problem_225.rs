use std::collections::VecDeque;

struct MyStack {
    queue: VecDeque<i32>,
    reverse: VecDeque<i32>,
    top: i32,
}

impl MyStack {
    fn new() -> Self {
        MyStack {
            queue: VecDeque::new(),
            reverse: VecDeque::new(),
            top: -1,
        }
    }

    fn push(&mut self, x: i32) {
        self.queue.push_back(x);
        self.top = x;
    }

    fn pop(&mut self) -> i32 {
        while self.queue.len() > 1 {
            // Impossible to get empty case here, as size is guarded by while loop condition
            let temp = self.queue.pop_front().unwrap();
            self.reverse.push_back(temp);
            self.top = temp;
        }
        let result = self.queue.pop_front();
        std::mem::swap(&mut self.queue, &mut self.reverse);
        return result.unwrap();
    }

    fn top(&self) -> i32 {
        self.top
    }

    fn empty(&self) -> bool {
        self.queue.len() == 0
    }
}
