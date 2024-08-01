# Leetcode submission id:https://leetcode.com/submissions/detail/1341057308/

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)


    def pop(self):
        self.peek() 
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self):
        return not self.stack1 and not self.stack2

myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
print(myQueue.peek())   
print(myQueue.pop())    
print(myQueue.empty())