"""
Queue and Deque Data Structure Templates
FIFO (First In First Out) for Queue, FILO for Deque
"""


class Node:
    """Node class for linked list based structures"""
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class QueueArray:
    """Queue implementation using Array with FIFO behavior"""
    
    def __init__(self, capacity=100):
        """Initialize queue with given capacity"""
        self.capacity = capacity
        self.queue = []
        self.front = 0
        self.rear = -1
    
    def enqueue(self, value):
        """Add element to rear of queue. Returns True on success, False if full."""
        if self.is_full():
            print("Queue Overflow: Cannot enqueue")
            return False
        self.queue.append(value)
        self.rear += 1
        return True
    
    def dequeue(self):
        """Remove and return element from front of queue. Returns None if empty."""
        if self.is_empty():
            print("Queue Underflow: Cannot dequeue from empty queue")
            return None
        value = self.queue.pop(0)
        self.rear -= 1
        return value
    
    def peek(self):
        """View front element without removing. Returns None if empty."""
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[0]
    
    def is_empty(self):
        """Check if queue is empty"""
        return self.rear == -1
    
    def is_full(self):
        """Check if queue is full"""
        return (self.rear + 1) >= self.capacity
    
    def size(self):
        """Get current size of queue"""
        return self.rear + 1 if not self.is_empty() else 0
    
    def display(self):
        """Display all elements in queue"""
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue (front to rear):", end=" ")
        for element in self.queue:
            print(element, end=" ")
        print()


class CircularQueue:
    """Circular Queue implementation using Array"""
    
    def __init__(self, capacity=100):
        """Initialize circular queue"""
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
    
    def enqueue(self, value):
        """Add element to rear of circular queue. Returns True on success."""
        if self.is_full():
            print("Queue Overflow: Cannot enqueue")
            return False
        
        if self.front == -1:
            self.front = 0
        
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        return True
    
    def dequeue(self):
        """Remove and return element from front. Returns None if empty."""
        if self.is_empty():
            print("Queue Underflow: Cannot dequeue from empty queue")
            return None
        
        value = self.queue[self.front]
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        
        return value
    
    def peek(self):
        """View front element without removing. Returns None if empty."""
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]
    
    def is_empty(self):
        """Check if queue is empty"""
        return self.front == -1
    
    def is_full(self):
        """Check if queue is full"""
        return (self.rear + 1) % self.capacity == self.front
    
    def display(self):
        """Display all elements in circular queue"""
        if self.is_empty():
            print("Queue is empty")
            return
        
        print("Circular Queue (front to rear):", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()



class QueueLinkedList:
    """Queue implementation using Linked List with FIFO behavior"""
    
    def __init__(self):
        """Initialize empty queue"""
        self.front = None
        self.rear = None
    
    def enqueue(self, value):
        """Add element to rear"""
        new_node = Node(value)
        
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        return True
    
    def dequeue(self):
        """Remove and return element from front. Returns None if empty."""
        if self.is_empty():
            print("Queue Underflow: Cannot dequeue from empty queue")
            return None
        
        value = self.front.value
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        
        return value
    
    def peek(self):
        """View front element without removing. Returns None if empty."""
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.front.value
    
    def is_empty(self):
        """Check if queue is empty"""
        return self.front is None
    
    def display(self):
        """Display all elements in queue"""
        if self.is_empty():
            print("Queue is empty")
            return
        
        print("Queue (front to rear):", end=" ")
        current = self.front
        while current:
            print(current.value, end=" ")
            current = current.next
        print()



class DequeArray:
    """Deque (Double Ended Queue) implementation using Array"""
    
    def __init__(self, capacity=100):
        """Initialize deque with given capacity"""
        self.capacity = capacity
        self.deque = []
        self.front = 0
        self.rear = -1
    
    def insert_front(self, value):
        """Insert element at front. Returns True on success, False if full."""
        if self.is_full():
            print("Deque Overflow: Cannot insert at front")
            return False
        self.deque.insert(0, value)
        self.rear += 1
        return True
    
    def insert_rear(self, value):
        """Insert element at rear. Returns True on success, False if full."""
        if self.is_full():
            print("Deque Overflow: Cannot insert at rear")
            return False
        self.deque.append(value)
        self.rear += 1
        return True
    
    def delete_front(self):
        """Delete and return element from front. Returns None if empty."""
        if self.is_empty():
            print("Deque Underflow: Cannot delete from front")
            return None
        value = self.deque.pop(0)
        self.rear -= 1
        return value
    
    def delete_rear(self):
        """Delete and return element from rear. Returns None if empty."""
        if self.is_empty():
            print("Deque Underflow: Cannot delete from rear")
            return None
        value = self.deque.pop()
        self.rear -= 1
        return value
    
    def get_front(self):
        """Get element at front without removing. Returns None if empty."""
        if self.is_empty():
            print("Deque is empty")
            return None
        return self.deque[0]
    
    def get_rear(self):
        """Get element at rear without removing. Returns None if empty."""
        if self.is_empty():
            print("Deque is empty")
            return None
        return self.deque[self.rear]
    
    def is_empty(self):
        """Check if deque is empty"""
        return self.rear == -1
    
    def is_full(self):
        """Check if deque is full"""
        return (self.rear + 1) >= self.capacity
    
    def display(self):
        """Display all elements in deque"""
        if self.is_empty():
            print("Deque is empty")
            return
        print("Deque (front to rear):", end=" ")
        for element in self.deque:
            print(element, end=" ")
        print()



class DequeLinkedList:
    """Deque (Double Ended Queue) implementation using Linked List"""
    
    def __init__(self):
        """Initialize empty deque"""
        self.front = None
        self.rear = None
    
    def insert_front(self, value):
        """Insert element at front"""
        new_node = Node(value)
        
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        return True
    
    def insert_rear(self, value):
        """Insert element at rear"""
        new_node = Node(value)
        
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        return True
    
    def delete_front(self):
        """Delete and return element from front. Returns None if empty."""
        if self.is_empty():
            print("Deque Underflow: Cannot delete from front")
            return None
        
        value = self.front.value
        
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        
        return value
    
    def delete_rear(self):
        """Delete and return element from rear. Returns None if empty."""
        if self.is_empty():
            print("Deque Underflow: Cannot delete from rear")
            return None
        
        value = self.rear.value
        
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        
        return value
    
    def get_front(self):
        """Get element at front without removing. Returns None if empty."""
        if self.is_empty():
            print("Deque is empty")
            return None
        return self.front.value
    
    def get_rear(self):
        """Get element at rear without removing. Returns None if empty."""
        if self.is_empty():
            print("Deque is empty")
            return None
        return self.rear.value
    
    def is_empty(self):
        """Check if deque is empty"""
        return self.front is None
    
    def display(self):
        """Display all elements in deque"""
        if self.is_empty():
            print("Deque is empty")
            return
        
        print("Deque (front to rear):", end=" ")
        current = self.front
        while current:
            print(current.value, end=" ")
            current = current.next
        print()
