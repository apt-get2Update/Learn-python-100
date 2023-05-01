<div align="center">
  <h1>   Learn Python: Queue</h1>
</div>



## Queue

This article covers queue implementation in Python. A queue is a linear data structure that follows the FIFO (First–In, First–Out) order, i.e., the item inserted first will be the first one out.

A queue supports the following standard operations:

- enqueue: Inserts an element at the rear (right side) of the queue.
- dequeue: Removes the element from the front (left side) of the queue and returns it.
- peek: Returns the element at the front of the queue without removing it.
- isEmpty: Checks whether the queue is empty.
- size: Returns the total number of elements present in the queue.


![queue_image](https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/440px-Data_Queue.svg.png)


<table>
  <tr>
    <th>Algorithm</th>
    <th>Average</th>
    <th>Worst case</th>
  </tr>
  <tr>
    <td>Space</td>
    <td>O(n)</td>
    <td>O(n)</td>
  </tr>
  <tr>
    <td>Search</td>
    <td>O(n)</td>
    <td>O(n)</td>
  </tr>
  <tr>
    <td>Insert</td>
    <td>O(1)</td>
    <td>O(1)</td>
  </tr>
  <tr>
    <td>Delete</td>
    <td>O(1)</td>
    <td>O(1)</td>
  </tr>
</table>


```sh
# Custom queue implementation in Python
class Queue:
 
    # Initialize queue
    def __init__(self, size=1000):
        self.q = [None] * size      # list to store queue elements
        self.capacity = size        # maximum capacity of the queue
        self.front = 0              # front points to the front element in the queue
        self.rear = -1              # rear points to the last element in the queue
        self.count = 0              # current size of the queue
 
    # Function to dequeue the front element
    def dequeue(self):
        # check for queue underflow
        if self.isEmpty():
            print('Queue Underflow!! Terminating process.')
            exit(-1)
        x = self.q[self.front]
        print('Removing element…', x)
        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1
        return x
 
    # Function to add an element to the queue
    def enqueue(self, value):
        # check for queue overflow
        if self.isFull():
            print('Overflow!! Terminating process.')
            exit(-1)
        print('Inserting element…', value)
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.count = self.count + 1
 
    # Function to return the front element of the queue
    def peek(self):
        if self.isEmpty():
            print('Queue UnderFlow!! Terminating process.')
            exit(-1)
        return self.q[self.front]
 
    # Function to return the size of the queue
    def size(self):
        return self.count
 
    # Function to check if the queue is empty or not
    def isEmpty(self):
        return self.size() == 0
 
    # Function to check if the queue is full or not
    def isFull(self):
        return self.size() == self.capacity
 
 
if __name__ == '__main__':
 
    # create a queue of capacity 5
    q = Queue(5)
 
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
 
    print('The queue size is', q.size())
    print('The front element is', q.peek())
    q.dequeue()
    print('The front element is', q.peek())
 
    q.dequeue()
    q.dequeue()
 
    if q.isEmpty():
        print('The queue is empty')
    else:
        print('The queue is not empty')

```