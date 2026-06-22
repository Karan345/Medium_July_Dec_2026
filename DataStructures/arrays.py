"""
Array Data Structure Template
Dynamic arrays (lists) and static arrays
"""


class Array:
    """
    Simple fixed-size array implementation.
    """

    def __init__(self, size=None):
        """Initialize an array. If size is provided, create fixed capacity.
        Otherwise create an empty array that behaves like a simple list.
        """
        if size is None:
            # behave like a simple Python list wrapper
            self._data = []
            self.capacity = None
        else:
            if size < 0:
                raise ValueError("size must be non-negative")
            self._data = [None] * size
            self.capacity = size
        self.length = 0

    def insert(self, index, value):
        """Insert element at given index. Returns True on success, False if out of bounds or full.
        If capacity is None (no fixed size), behaves like list.insert.
        """
        if index < 0 or index > self.length:
            raise IndexError("index out of range")

        if self.capacity is not None:
            if self.length >= self.capacity:
                # cannot grow
                print("Array Overflow: cannot insert")
                return False
            # shift right
            for i in range(self.length, index, -1):
                self._data[i] = self._data[i - 1]
            self._data[index] = value
            self.length += 1
            return True
        else:
            self._data.insert(index, value)
            self.length = len(self._data)
            return True

    def delete(self, index):
        """Delete element at given index and return it. Raises IndexError if invalid."""
        if index < 0 or index >= self.length:
            raise IndexError("index out of range")

        if self.capacity is not None:
            value = self._data[index]
            # shift left
            for i in range(index, self.length - 1):
                self._data[i] = self._data[i + 1]
            self._data[self.length - 1] = None
            self.length -= 1
            return value
        else:
            value = self._data.pop(index)
            self.length = len(self._data)
            return value

    def search(self, value):
        """Search for an element and return its index, or -1 if not found."""
        for i in range(self.length):
            if self._data[i] == value:
                return i
        return -1

    def traverse(self):
        """Return a list of current elements (for printing/testing)."""
        return [self._data[i] for i in range(self.length)]

    def update(self, index, value):
        """Update element at given index. Raises IndexError if invalid."""
        if index < 0 or index >= self.length:
            raise IndexError("index out of range")
        self._data[index] = value
        return True

    def get(self, index):
        """Get element at given index. Raises IndexError if invalid."""
        if index < 0 or index >= self.length:
            raise IndexError("index out of range")
        return self._data[index]


class DynamicArray:
    """
    Dynamic array implementation with automatic resizing.
    """

    def __init__(self, capacity=10):
        """Initialize with initial capacity."""
        if capacity <= 0:
            capacity = 1
        self.capacity = capacity
        self._data = [None] * self.capacity
        self.length = 0

    def append(self, value):
        """Add element to the end, resizing if necessary."""
        if self.length >= self.capacity:
            self.resize(self.capacity * 2)
        self._data[self.length] = value
        self.length += 1
        return True

    def pop(self):
        """Remove and return last element; return None if empty."""
        if self.length == 0:
            print("Array Underflow: cannot pop from empty array")
            return None
        value = self._data[self.length - 1]
        self._data[self.length - 1] = None
        self.length -= 1
        # shrink if too sparse
        if self.length > 0 and self.length <= self.capacity // 4:
            new_cap = max(self.capacity // 2, 1)
            self.resize(new_cap)
        return value

    def resize(self, new_capacity):
        """Resize internal storage to new_capacity (>= current length)."""
        if new_capacity < self.length:
            raise ValueError("new capacity must be >= number of elements")
        new_array = [None] * new_capacity
        for i in range(self.length):
            new_array[i] = self._data[i]
        self._data = new_array
        self.capacity = new_capacity
        return True

    def __getitem__(self, index):
        """Get element by index (supports negative indices)."""
        if index < 0:
            index = self.length + index
        if index < 0 or index >= self.length:
            raise IndexError("index out of range")
        return self._data[index]

    def __setitem__(self, index, value):
        """Set element by index (supports negative indices)."""
        if index < 0:
            index = self.length + index
        if index < 0 or index >= self.length:
            raise IndexError("index out of range")
        self._data[index] = value
        return True

    def __len__(self):
        return self.length

    def to_list(self):
        """Return a Python list of current elements."""
        return [self._data[i] for i in range(self.length)]
