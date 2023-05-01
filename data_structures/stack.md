<div align="center">
  <h1>   Learn Python: Stack</h1>
</div>



## Stack

A stack is a linear data structure that follows the LIFO (Last–In, First–Out) order, i.e., items can be inserted or removed only at one end of it.

The stack supports the following standard operations:

- push: Pushes an item at the top of the stack.
- pop: Remove and return the item from the top of the stack.
- peek: Returns the item at the top of the stack without removing it.
- size: Returns the total number of items in the stack.
- isEmpty: Checks whether the stack is empty.
- isFull: Checks whether the stack is full.


![stack_image](https://upload.wikimedia.org/wikipedia/commons/2/29/Data_stack.svg)

```sh
class Stack:
 
    # Constructor to initialize the stack
    def __init__(self, size):
        self.arr = [None] * size
        self.capacity = size
        self.top = -1
 
    # Function to add an element `val` to the stack
    def push(self, val):
        if self.isFull():
            print('Stack Overflow!! Calling exit()…')
            exit(-1)
 
        print(f'Inserting {val} into the stack…')
        self.top = self.top + 1
        self.arr[self.top] = val
 
    # Function to pop a top element from the stack
    def pop(self):
        # check for stack underflow
        if self.isEmpty():
            print('Stack Underflow!! Calling exit()…')
            exit(-1)
 
        print(f'Removing {self.peek()} from the stack')
 
        # decrease stack size by 1 and (optionally) return the popped element
        top = self.arr[self.top]
        self.top = self.top - 1
        return top
 
    # Function to return the top element of the stack
    def peek(self):
        if self.isEmpty():
            exit(-1)
        return self.arr[self.top]
 
    # Function to return the size of the stack
    def size(self):
        return self.top + 1
 
    # Function to check if the stack is empty or not
    def isEmpty(self):
        return self.size() == 0
 
    # Function to check if the stack is full or not
    def isFull(self):
        return self.size() == self.capacity
 
 
if __name__ == '__main__':
 
    stack = Stack(3)
 
    stack.push(1)       # Inserting 1 in the stack
    stack.push(2)       # Inserting 2 in the stack
 
    stack.pop()         # removing the top element (2)
    stack.pop()         # removing the top element (1)
 
    stack.push(3)       # Inserting 3 in the stack
 
    print('Top element is', stack.peek())
    print('The stack size is', stack.size())
 
    stack.pop()         # removing the top element (3)
 
    # check if the stack is empty
    if stack.isEmpty():
        print('The stack is empty')
    else:
        print('The stack is not empty')

```