"""
Stack is abstract data type
 - push(v) to add value to top of stack
 - pop() removes topmost value and returns it
 - isEmpty() determines if stack is empty

Use Example to demonstrate approach

"""


class Stack:
    def __init__(self):
        """Demonstrate using list as storage for a Stack."""
        self.stack = []

    def isEmpty(self):
        """ Determines whether stack is Empty."""
        return len(self.stack) == 0

    def push(self, v):
        """push v onto the stack. O(1) performance."""
        self.stack.append(v)

    def pop(self):
        """ Remove topmost element and return it. O(1) performance."""
        if self.isEmpty():
            raise Exception('Stack is empty.')
        return self.stack.pop()

    def __repr__(self):
        return "stack:" + str(self.stack)


"""  Test  """

s = Stack()
s.push(3)
s.push(4)
print(s)
s.pop()
# print(s)
"""
s.push(1)
s.push(3)
s.push(5)
s
stack:[1, 3, 5]
s.pop()
5
s.pop()
3
s.pop()
1
s.pop()

"""

"""
Stack Summary

Design new data type
    - Storing information using built-in types
    - Define separate interface to avoid programmer error
    
Identify supported operations
    - Document performance Using O(n) notation
"""
