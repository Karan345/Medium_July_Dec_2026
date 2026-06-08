"""
Heap and Priority Queue Data Structure Templates
Min Heap, Max Heap, Binary Heap, and Priority Queue
"""


class MinHeap:
    """Template for Min Heap"""
    
    def __init__(self):
        """Initialize empty min heap"""
        self.heap = []
    
    def parent(self, index):
        """Get parent index"""
        return (index - 1) // 2
    
    def left_child(self, index):
        """Get left child index"""
        return 2 * index + 1
    
    def right_child(self, index):
        """Get right child index"""
        return 2 * index + 2
    
    def swap(self, i, j):
        """Swap two elements"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def heapify_up(self, index):
        """Bubble up element to maintain heap property"""
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.swap(index, self.parent(index))
            index = self.parent(index)
    
    def heapify_down(self, index):
        """Bubble down element to maintain heap property"""
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != index:
            self.swap(index, smallest)
            self.heapify_down(smallest)
    
    def insert(self, value):
        """Insert value into heap"""
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
    
    def extract_min(self):
        """Remove and return minimum element"""
        if self.is_empty():
            return None
        
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if not self.is_empty():
            self.heapify_down(0)
        
        return min_val
    
    def peek_min(self):
        """Get minimum element without removing"""
        return self.heap[0] if not self.is_empty() else None
    
    def is_empty(self):
        """Check if heap is empty"""
        return len(self.heap) == 0
    
    def size(self):
        """Get heap size"""
        return len(self.heap)
    
    def build_heap(self, array):
        """Build heap from array"""
        self.heap = array[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)


class MaxHeap:
    """Template for Max Heap"""
    
    def __init__(self):
        """Initialize empty max heap"""
        self.heap = []
    
    def parent(self, index):
        """Get parent index"""
        return (index - 1) // 2
    
    def left_child(self, index):
        """Get left child index"""
        return 2 * index + 1
    
    def right_child(self, index):
        """Get right child index"""
        return 2 * index + 2
    
    def swap(self, i, j):
        """Swap two elements"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def heapify_up(self, index):
        """Bubble up element"""
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.swap(index, self.parent(index))
            index = self.parent(index)
    
    def heapify_down(self, index):
        """Bubble down element"""
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)
        
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        
        if largest != index:
            self.swap(index, largest)
            self.heapify_down(largest)
    
    def insert(self, value):
        """Insert value into heap"""
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
    
    def extract_max(self):
        """Remove and return maximum element"""
        if self.is_empty():
            return None
        
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if not self.is_empty():
            self.heapify_down(0)
        
        return max_val
    
    def peek_max(self):
        """Get maximum element without removing"""
        return self.heap[0] if not self.is_empty() else None
    
    def is_empty(self):
        """Check if heap is empty"""
        return len(self.heap) == 0
    
    def size(self):
        """Get heap size"""
        return len(self.heap)


class PriorityQueue:
    """Template for Priority Queue using Min Heap"""
    
    def __init__(self):
        """Initialize empty priority queue"""
        self.heap = []
    
    def _parent(self, index):
        """Get parent index"""
        return (index - 1) // 2
    
    def _left_child(self, index):
        """Get left child index"""
        return 2 * index + 1
    
    def _right_child(self, index):
        """Get right child index"""
        return 2 * index + 2
    
    def _swap(self, i, j):
        """Swap two elements"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def _heapify_up(self, index):
        """Bubble up element"""
        while index > 0 and self.heap[self._parent(index)][1] > self.heap[index][1]:
            self._swap(index, self._parent(index))
            index = self._parent(index)
    
    def _heapify_down(self, index):
        """Bubble down element"""
        smallest = index
        left = self._left_child(index)
        right = self._right_child(index)
        
        if left < len(self.heap) and self.heap[left][1] < self.heap[smallest][1]:
            smallest = left
        
        if right < len(self.heap) and self.heap[right][1] < self.heap[smallest][1]:
            smallest = right
        
        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)
    
    def enqueue(self, value, priority):
        """Add element with priority"""
        self.heap.append((value, priority))
        self._heapify_up(len(self.heap) - 1)
    
    def dequeue(self):
        """Remove and return highest priority element"""
        if self.is_empty():
            return None
        
        value, priority = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if not self.is_empty():
            self._heapify_down(0)
        
        return value
    
    def peek(self):
        """View highest priority element"""
        return self.heap[0][0] if not self.is_empty() else None
    
    def update_priority(self, value, new_priority):
        """Update priority of element"""
        for i in range(len(self.heap)):
            if self.heap[i][0] == value:
                old_priority = self.heap[i][1]
                self.heap[i] = (value, new_priority)
                
                if new_priority < old_priority:
                    self._heapify_up(i)
                else:
                    self._heapify_down(i)
                return True
        
        return False
    
    def is_empty(self):
        """Check if queue is empty"""
        return len(self.heap) == 0
    
    def size(self):
        """Get queue size"""
        return len(self.heap)


class HeapSort:
    """Template for Heap Sort algorithm"""
    
    @staticmethod
    def heap_sort(array):
        """Sort array using heap sort"""
        if not array:
            return array
        
        HeapSort.build_max_heap(array)
        
        for i in range(len(array) - 1, 0, -1):
            array[0], array[i] = array[i], array[0]
            HeapSort.heapify(array, 0, i)
        
        return array
    
    @staticmethod
    def build_max_heap(array):
        """Build max heap from array"""
        for i in range(len(array) // 2 - 1, -1, -1):
            HeapSort.heapify(array, i, len(array))
    
    @staticmethod
    def heapify(array, index, heap_size):
        """Heapify subtree"""
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < heap_size and array[left] > array[largest]:
            largest = left
        
        if right < heap_size and array[right] > array[largest]:
            largest = right
        
        if largest != index:
            array[index], array[largest] = array[largest], array[index]
            HeapSort.heapify(array, largest, heap_size)
