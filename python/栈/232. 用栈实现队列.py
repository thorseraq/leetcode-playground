class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)
        # print(f'after push: {self.stack1}')


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return None
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        temp = self.stack2.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())

        # print(f'after pop: {self.stack1}')
        return temp
    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return None
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        temp = self.stack2[-1]

        while self.stack2:
            self.stack1.append(self.stack2.pop())

        # print(f'after peek: {self.stack1}')
        return temp

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not bool(self.stack1)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()