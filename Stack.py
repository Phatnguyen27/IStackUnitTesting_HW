import numpy as np

class IStack:
    def clear(self):
        raise NotImplementedError()
    def contains(self,item):
        raise NotImplementedError()
    def pop(self):
        raise NotImplementedError()
    def push(self,item):
        raise NotImplementedError()
    def peek(self):
        raise NotImplementedError()
    def isEmpty(self):
        raise NotImplementedError()

class MyStack(IStack):
    def __init__(self):
        self.data = []
    def clear(self):
        if self.isEmpty():
            raise StackEmptyException('Stack is empty')
        self.data.clear()
    def contains(self, item):
        return True if any(np.asarray(self.data) == item) else False
    def push(self, item):
        if not isinstance(item,str):
            raise TypeError('Only string is allowed')
        self.data.append(item)
    def pop(self):
        if self.isEmpty():
            raise StackEmptyException('Stack is empty')
        result = self.data[-1]
        del(self.data[-1])
        return result
    def peek(self):
        if self.isEmpty():
            raise StackEmptyException('Stack is empty')
    def isEmpty(self):
        return True if len(self.data) <= 0 else False
    def display(self):
        if self.isEmpty():
            print('Stack if empty')
        else:
            print(self.data)

class StackEmptyException(Exception):
    pass