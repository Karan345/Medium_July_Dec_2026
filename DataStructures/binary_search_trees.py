"""
Binary Search Tree (BST) Data Structure Template
"""


class TreeNode:
    """Node class for Binary Search Tree"""
    
    def __init__(self, value):
        """Initialize a tree node"""
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Template for Binary Search Tree"""
    
    def __init__(self):
        """Initialize empty BST"""
        self.root = None
    
    def insert(self, value):
        """Insert a value into BST"""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """Helper function to insert recursively"""
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        """Search for a value in BST"""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """Helper function to search recursively"""
        if node is None:
            return False
        
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def delete(self, value):
        """Delete a value from BST"""
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        """Helper function to delete recursively"""
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with one or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children: get inorder successor (smallest in right subtree)
            min_larger_node = self._find_min_node(node.right)
            node.value = min_larger_node.value
            node.right = self._delete_recursive(node.right, min_larger_node.value)
        
        return node
    
    def _find_min_node(self, node):
        """Find node with minimum value"""
        current = node
        while current.left:
            current = current.left
        return current
    
    def inorder_traversal(self):
        """In-order traversal (Left-Root-Right)"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper function for inorder traversal"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self):
        """Pre-order traversal (Root-Left-Right)"""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        """Helper function for preorder traversal"""
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self):
        """Post-order traversal (Left-Right-Root)"""
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        """Helper function for postorder traversal"""
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)
    
    def level_order_traversal(self):
        """Level-order (Breadth-first) traversal"""
        if not self.root:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def find_min(self):
        """Find minimum value"""
        if not self.root:
            return None
        return self._find_min_node(self.root).value
    
    def find_max(self):
        """Find maximum value"""
        if not self.root:
            return None
        
        current = self.root
        while current.right:
            current = current.right
        return current.value
    
    def height(self):
        """Get height of tree"""
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        """Helper function to calculate height"""
        if node is None:
            return -1
        return 1 + max(self._height_recursive(node.left), self._height_recursive(node.right))
    
    def is_balanced(self):
        """Check if tree is balanced"""
        return self._is_balanced_recursive(self.root)[0]
    
    def _is_balanced_recursive(self, node):
        """Helper function to check if tree is balanced"""
        if node is None:
            return True, -1
        
        left_balanced, left_height = self._is_balanced_recursive(node.left)
        if not left_balanced:
            return False, 0
        
        right_balanced, right_height = self._is_balanced_recursive(node.right)
        if not right_balanced:
            return False, 0
        
        is_balanced = abs(left_height - right_height) <= 1
        height = 1 + max(left_height, right_height)
        
        return is_balanced, height
    
    def is_bst(self):
        """Verify if tree is a valid BST"""
        return self._is_bst_recursive(self.root, float('-inf'), float('inf'))
    
    def _is_bst_recursive(self, node, min_val, max_val):
        """Helper function to validate BST property"""
        if node is None:
            return True
        
        if node.value <= min_val or node.value >= max_val:
            return False
        
        return (self._is_bst_recursive(node.left, min_val, node.value) and
                self._is_bst_recursive(node.right, node.value, max_val))
    
    def find_kth_smallest(self, k):
        """Find kth smallest element"""
        self.kth_counter = 0
        result = []
        self._kth_smallest_helper(self.root, k, result)
        return result[0] if result else None
    
    def _kth_smallest_helper(self, node, k, result):
        """Helper for finding kth smallest"""
        if not node or result:
            return
        
        self._kth_smallest_helper(node.left, k, result)
        
        self.kth_counter += 1
        if self.kth_counter == k:
            result.append(node.value)
            return
        
        self._kth_smallest_helper(node.right, k, result)
    
    def find_kth_largest(self, k):
        """Find kth largest element"""
        self.kth_counter = 0
        result = []
        self._kth_largest_helper(self.root, k, result)
        return result[0] if result else None
    
    def _kth_largest_helper(self, node, k, result):
        """Helper for finding kth largest"""
        if not node or result:
            return
        
        self._kth_largest_helper(node.right, k, result)
        
        self.kth_counter += 1
        if self.kth_counter == k:
            result.append(node.value)
            return
        
        self._kth_largest_helper(node.left, k, result)
    
    def lowest_common_ancestor(self, node1, node2):
        """Find LCA of two nodes"""
        return self._lca_recursive(self.root, node1, node2)
    
    def _lca_recursive(self, node, node1, node2):
        """Helper to find LCA"""
        if node is None:
            return None
        
        if node1 < node.value and node2 < node.value:
            return self._lca_recursive(node.left, node1, node2)
        elif node1 > node.value and node2 > node.value:
            return self._lca_recursive(node.right, node1, node2)
        else:
            return node.value
    
    def is_ancestor(self, ancestor, node):
        """Check if node is ancestor"""
        return self._is_ancestor_helper(self.root, ancestor, node)
    
    def _is_ancestor_helper(self, root, ancestor, node):
        """Helper to check ancestor relationship"""
        if not root:
            return False
        
        if root.value == ancestor:
            return self._find_node(root, node)
        
        if ancestor < root.value:
            return self._is_ancestor_helper(root.left, ancestor, node)
        else:
            return self._is_ancestor_helper(root.right, ancestor, node)
    
    def _find_node(self, node, value):
        """Helper to find if value exists in subtree"""
        if not node:
            return False
        
        if node.value == value:
            return True
        
        return (self._find_node(node.left, value) or
                self._find_node(node.right, value))


class AVL_Node:
    """Node for AVL Tree (included here for reference)"""
    
    def __init__(self, value):
        """Initialize AVL node"""
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
