"""
Hash Table Data Structure Template
Hash Functions, Collision Handling, and Operations
"""


class HashTable:
    """Template for Hash Table with separate chaining"""
    
    def __init__(self, size=100):
        """Initialize hash table with given size"""
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        """Hash function to compute index"""
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insert key-value pair"""
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
    
    def search(self, key):
        """Search for a key"""
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return True
        return False
    
    def delete(self, key):
        """Delete a key-value pair"""
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                return True
        return False
    
    def display(self):
        """Display all key-value pairs"""
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {i}: {bucket}")
    
    def get(self, key):
        """Get value for given key"""
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None


class OpenAddressingHashTable:
    """Template for Hash Table with Open Addressing (Linear Probing)"""
    
    def __init__(self, size=100):
        """Initialize hash table"""
        self.size = size
        self.table = [None] * size
        self.occupied = [False] * size
    
    def hash_function(self, key):
        """Hash function"""
        return hash(key) % self.size
    
    def linear_probe(self, index):
        """Linear probing for collision resolution"""
        probes = 0
        while self.occupied[index] and probes < self.size:
            index = (index + 1) % self.size
            probes += 1
        return index if probes < self.size else -1
    
    def insert(self, key, value):
        """Insert key-value pair"""
        index = self.hash_function(key)
        
        # Check if key already exists
        original_index = index
        while self.occupied[index]:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
            if index == original_index:
                print("Hash table is full")
                return
        
        self.table[index] = (key, value)
        self.occupied[index] = True
    
    def search(self, key):
        """Search for a key"""
        index = self.hash_function(key)
        original_index = index
        
        while self.occupied[index]:
            if self.table[index][0] == key:
                return True
            index = (index + 1) % self.size
            if index == original_index:
                break
        return False
    
    def delete(self, key):
        """Delete a key-value pair"""
        index = self.hash_function(key)
        original_index = index
        
        while self.occupied[index]:
            if self.table[index][0] == key:
                self.table[index] = None
                self.occupied[index] = False
                return True
            index = (index + 1) % self.size
            if index == original_index:
                break
        return False
    
    def display(self):
        """Display all key-value pairs"""
        for i, pair in enumerate(self.table):
            if pair:
                print(f"Index {i}: {pair}")


class QuadraticProbingHashTable:
    """Template for Hash Table with Quadratic Probing"""
    
    def __init__(self, size=100):
        """Initialize hash table"""
        self.size = size
        self.table = [None] * size
        self.occupied = [False] * size
    
    def hash_function(self, key):
        """Hash function"""
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insert key-value pair"""
        index = self.hash_function(key)
        i = 0
        
        while i < self.size:
            probe_index = (index + i * i) % self.size
            
            if not self.occupied[probe_index]:
                self.table[probe_index] = (key, value)
                self.occupied[probe_index] = True
                return
            elif self.table[probe_index][0] == key:
                self.table[probe_index] = (key, value)
                return
            
            i += 1
        
        print("Hash table is full")
    
    def search(self, key):
        """Search for a key"""
        index = self.hash_function(key)
        i = 0
        
        while i < self.size:
            probe_index = (index + i * i) % self.size
            
            if not self.occupied[probe_index]:
                return False
            
            if self.table[probe_index][0] == key:
                return True
            
            i += 1
        
        return False
    
    def delete(self, key):
        """Delete a key-value pair"""
        index = self.hash_function(key)
        i = 0
        
        while i < self.size:
            probe_index = (index + i * i) % self.size
            
            if not self.occupied[probe_index]:
                return False
            
            if self.table[probe_index][0] == key:
                self.table[probe_index] = None
                self.occupied[probe_index] = False
                return True
            
            i += 1
        
        return False


class DoubleHashingHashTable:
    """Template for Hash Table with Double Hashing"""
    
    def __init__(self, size=100):
        """Initialize hash table"""
        self.size = size
        self.table = [None] * size
        self.occupied = [False] * size
    
    def hash_function1(self, key):
        """Primary hash function"""
        return hash(key) % self.size
    
    def hash_function2(self, key):
        """Secondary hash function"""
        return 7 - (hash(key) % 7)
    
    def insert(self, key, value):
        """Insert key-value pair"""
        index = self.hash_function1(key)
        step = self.hash_function2(key)
        i = 0
        
        while i < self.size:
            probe_index = (index + i * step) % self.size
            
            if not self.occupied[probe_index]:
                self.table[probe_index] = (key, value)
                self.occupied[probe_index] = True
                return
            elif self.table[probe_index][0] == key:
                self.table[probe_index] = (key, value)
                return
            
            i += 1
        
        print("Hash table is full")
    
    def search(self, key):
        """Search for a key"""
        index = self.hash_function1(key)
        step = self.hash_function2(key)
        i = 0
        
        while i < self.size:
            probe_index = (index + i * step) % self.size
            
            if not self.occupied[probe_index]:
                return False
            
            if self.table[probe_index][0] == key:
                return True
            
            i += 1
        
        return False
    
    def delete(self, key):
        """Delete a key-value pair"""
        index = self.hash_function1(key)
        step = self.hash_function2(key)
        i = 0
        
        while i < self.size:
            probe_index = (index + i * step) % self.size
            
            if not self.occupied[probe_index]:
                return False
            
            if self.table[probe_index][0] == key:
                self.table[probe_index] = None
                self.occupied[probe_index] = False
                return True
            
            i += 1
        
        return False
