# Leetcode submission id:https://leetcode.com/submissions/detail/1341048421/

from collections import deque
class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        self.queue1.append(x)
        while self.queue2:
            self.queue1.append(self.queue2.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        return self.queue2.popleft()

    def top(self):
        return self.queue2[0]

    def empty(self):
        return not self.queue2
        

myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())   
print(myStack.pop())   
print(myStack.empty())