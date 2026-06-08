"""
Graph Data Structure Templates
Directed, Undirected Graphs and Graph Algorithms
"""


class GraphNode:
    """Node class for Graph"""
    
    def __init__(self, value):
        """Initialize graph node"""
        self.value = value
        self.neighbors = []


class UndirectedGraph:
    """Template for Undirected Graph using Adjacency List"""
    
    def __init__(self):
        """Initialize empty undirected graph"""
        self.vertices = {}
        self.edge_count = 0
    
    def add_vertex(self, vertex):
        """Add vertex to graph"""
        if vertex not in self.vertices:
            self.vertices[vertex] = []
    
    def remove_vertex(self, vertex):
        """Remove vertex from graph"""
        if vertex not in self.vertices:
            return False
        
        for neighbor in self.vertices[vertex]:
            self.vertices[neighbor].remove(vertex)
            self.edge_count -= 1
        
        del self.vertices[vertex]
        return True
    
    def add_edge(self, vertex1, vertex2, weight=1):
        """Add undirected edge between vertices"""
        if vertex1 not in self.vertices:
            self.add_vertex(vertex1)
        if vertex2 not in self.vertices:
            self.add_vertex(vertex2)
        
        if vertex2 not in self.vertices[vertex1]:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)
            self.edge_count += 1
    
    def remove_edge(self, vertex1, vertex2):
        """Remove edge between vertices"""
        if vertex1 in self.vertices and vertex2 in self.vertices[vertex1]:
            self.vertices[vertex1].remove(vertex2)
            self.vertices[vertex2].remove(vertex1)
            self.edge_count -= 1
            return True
        return False
    
    def get_neighbors(self, vertex):
        """Get neighbors of vertex"""
        return self.vertices.get(vertex, [])
    
    def has_edge(self, vertex1, vertex2):
        """Check if edge exists"""
        if vertex1 in self.vertices:
            return vertex2 in self.vertices[vertex1]
        return False
    
    def get_degree(self, vertex):
        """Get degree of vertex"""
        return len(self.vertices.get(vertex, []))
    
    def is_connected(self):
        """Check if graph is connected"""
        if not self.vertices:
            return True
        
        visited = set()
        start = next(iter(self.vertices))
        stack = [start]
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.vertices[vertex]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return len(visited) == len(self.vertices)


class DirectedGraph:
    """Template for Directed Graph using Adjacency List"""
    
    def __init__(self):
        """Initialize empty directed graph"""
        self.vertices = {}
        self.edge_count = 0
    
    def add_vertex(self, vertex):
        """Add vertex to graph"""
        if vertex not in self.vertices:
            self.vertices[vertex] = {'out': [], 'in': []}
    
    def remove_vertex(self, vertex):
        """Remove vertex from graph"""
        if vertex not in self.vertices:
            return False
        
        for out_vertex in self.vertices[vertex]['out']:
            self.vertices[out_vertex]['in'].remove(vertex)
            self.edge_count -= 1
        
        for in_vertex in self.vertices[vertex]['in']:
            self.vertices[in_vertex]['out'].remove(vertex)
            self.edge_count -= 1
        
        del self.vertices[vertex]
        return True
    
    def add_edge(self, from_vertex, to_vertex, weight=1):
        """Add directed edge from source to destination"""
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)
        
        if to_vertex not in self.vertices[from_vertex]['out']:
            self.vertices[from_vertex]['out'].append(to_vertex)
            self.vertices[to_vertex]['in'].append(from_vertex)
            self.edge_count += 1
    
    def remove_edge(self, from_vertex, to_vertex):
        """Remove edge"""
        if from_vertex in self.vertices and to_vertex in self.vertices[from_vertex]['out']:
            self.vertices[from_vertex]['out'].remove(to_vertex)
            self.vertices[to_vertex]['in'].remove(from_vertex)
            self.edge_count -= 1
            return True
        return False
    
    def get_out_neighbors(self, vertex):
        """Get outgoing neighbors"""
        return self.vertices.get(vertex, {}).get('out', [])
    
    def get_in_neighbors(self, vertex):
        """Get incoming neighbors"""
        return self.vertices.get(vertex, {}).get('in', [])
    
    def get_in_degree(self, vertex):
        """Get in-degree"""
        return len(self.vertices.get(vertex, {}).get('in', []))
    
    def get_out_degree(self, vertex):
        """Get out-degree"""
        return len(self.vertices.get(vertex, {}).get('out', []))
    
    def has_cycle(self):
        """Check if graph has cycle"""
        visited = set()
        rec_stack = set()
        
        def has_cycle_dfs(vertex):
            visited.add(vertex)
            rec_stack.add(vertex)
            
            for neighbor in self.vertices[vertex]['out']:
                if neighbor not in visited:
                    if has_cycle_dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
            
            rec_stack.remove(vertex)
            return False
        
        for vertex in self.vertices:
            if vertex not in visited:
                if has_cycle_dfs(vertex):
                    return True
        
        return False
    
    def is_dag(self):
        """Check if graph is DAG"""
        return not self.has_cycle()
    
    def topological_sort(self):
        """Return topological ordering"""
        visited = set()
        stack = []
        
        def dfs(vertex):
            visited.add(vertex)
            for neighbor in self.vertices[vertex]['out']:
                if neighbor not in visited:
                    dfs(neighbor)
            stack.append(vertex)
        
        for vertex in self.vertices:
            if vertex not in visited:
                dfs(vertex)
        
        return stack[::-1]


class WeightedGraph(UndirectedGraph):
    """Template for Weighted Undirected Graph"""
    
    def __init__(self):
        """Initialize weighted graph"""
        super().__init__()
        self.weights = {}
    
    def add_weighted_edge(self, vertex1, vertex2, weight):
        """Add weighted edge"""
        self.add_edge(vertex1, vertex2, weight)
        self.weights[(min(vertex1, vertex2), max(vertex1, vertex2))] = weight
    
    def get_edge_weight(self, vertex1, vertex2):
        """Get weight of edge"""
        key = (min(vertex1, vertex2), max(vertex1, vertex2))
        return self.weights.get(key, None)


class GraphTraversals:
    """Template for Graph traversal algorithms"""
    
    @staticmethod
    def bfs(graph, start):
        """Breadth-first search"""
        visited = set()
        queue = [start]
        result = []
        
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                neighbors = graph.get_neighbors(vertex) if hasattr(graph, 'get_neighbors') else graph.vertices.get(vertex, {}).get('out', [])
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return result
    
    @staticmethod
    def dfs(graph, start):
        """Depth-first search"""
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                neighbors = graph.get_neighbors(vertex) if hasattr(graph, 'get_neighbors') else graph.vertices.get(vertex, {}).get('out', [])
                for neighbor in reversed(neighbors):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result
    
    @staticmethod
    def dfs_recursive(graph, vertex, visited=None):
        """DFS using recursion"""
        if visited is None:
            visited = set()
        
        visited.add(vertex)
        result = [vertex]
        
        neighbors = graph.get_neighbors(vertex) if hasattr(graph, 'get_neighbors') else graph.vertices.get(vertex, {}).get('out', [])
        for neighbor in neighbors:
            if neighbor not in visited:
                result.extend(GraphTraversals.dfs_recursive(graph, neighbor, visited))
        
        return result


class GraphAlgorithms:
    """Template for Graph algorithms"""
    
    @staticmethod
    def dijkstra(graph, start):
        """Dijkstra's shortest path algorithm"""
        distances = {vertex: float('inf') for vertex in graph.vertices}
        distances[start] = 0
        visited = set()
        
        while len(visited) < len(graph.vertices):
            current = None
            for vertex in graph.vertices:
                if vertex not in visited and (current is None or distances[vertex] < distances[current]):
                    current = vertex
            
            if current is None or distances[current] == float('inf'):
                break
            
            visited.add(current)
            neighbors = graph.get_neighbors(current) if hasattr(graph, 'get_neighbors') else graph.vertices.get(current, {}).get('out', [])
            
            for neighbor in neighbors:
                weight = graph.get_edge_weight(current, neighbor) if hasattr(graph, 'get_edge_weight') else 1
                if distances[current] + weight < distances[neighbor]:
                    distances[neighbor] = distances[current] + weight
        
        return distances
    
    @staticmethod
    def bellman_ford(graph, start):
        """Bellman-Ford shortest path algorithm"""
        distances = {vertex: float('inf') for vertex in graph.vertices}
        distances[start] = 0
        
        for _ in range(len(graph.vertices) - 1):
            for vertex in graph.vertices:
                neighbors = graph.get_neighbors(vertex) if hasattr(graph, 'get_neighbors') else graph.vertices.get(vertex, {}).get('out', [])
                for neighbor in neighbors:
                    weight = graph.get_edge_weight(vertex, neighbor) if hasattr(graph, 'get_edge_weight') else 1
                    if distances[vertex] != float('inf') and distances[vertex] + weight < distances[neighbor]:
                        distances[neighbor] = distances[vertex] + weight
        
        return distances
    
    @staticmethod
    def floyd_warshall(graph):
        """Floyd-Warshall all-pairs shortest path"""
        vertices = list(graph.vertices.keys())
        n = len(vertices)
        dist = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            dist[i][i] = 0
        
        for i, vertex in enumerate(vertices):
            neighbors = graph.get_neighbors(vertex) if hasattr(graph, 'get_neighbors') else graph.vertices.get(vertex, {}).get('out', [])
            for neighbor in neighbors:
                j = vertices.index(neighbor)
                weight = graph.get_edge_weight(vertex, neighbor) if hasattr(graph, 'get_edge_weight') else 1
                dist[i][j] = weight
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        return dist
    
    @staticmethod
    def kruskal(graph):
        """Kruskal's MST algorithm"""
        edges = []
        for vertex in graph.vertices:
            neighbors = graph.get_neighbors(vertex) if hasattr(graph, 'get_neighbors') else graph.vertices.get(vertex, {}).get('out', [])
            for neighbor in neighbors:
                if vertex < neighbor:
                    weight = graph.get_edge_weight(vertex, neighbor) if hasattr(graph, 'get_edge_weight') else 1
                    edges.append((weight, vertex, neighbor))
        
        edges.sort()
        parent = {vertex: vertex for vertex in graph.vertices}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
                return True
            return False
        
        mst = []
        for weight, u, v in edges:
            if union(u, v):
                mst.append((u, v, weight))
        
        return mst
    
    @staticmethod
    def prim(graph, start):
        """Prim's MST algorithm"""
        visited = set([start])
        edges = []
        mst = []
        
        neighbors = graph.get_neighbors(start) if hasattr(graph, 'get_neighbors') else graph.vertices.get(start, {}).get('out', [])
        for neighbor in neighbors:
            weight = graph.get_edge_weight(start, neighbor) if hasattr(graph, 'get_edge_weight') else 1
            edges.append((weight, start, neighbor))
        
        edges.sort()
        
        while edges and len(visited) < len(graph.vertices):
            weight, u, v = edges.pop(0)
            
            if v not in visited:
                visited.add(v)
                mst.append((u, v, weight))
                
                neighbors = graph.get_neighbors(v) if hasattr(graph, 'get_neighbors') else graph.vertices.get(v, {}).get('out', [])
                for neighbor in neighbors:
                    if neighbor not in visited:
                        weight = graph.get_edge_weight(v, neighbor) if hasattr(graph, 'get_edge_weight') else 1
                        edges.append((weight, v, neighbor))
                
                edges.sort()
        
        return mst
    
    @staticmethod
    def dfs_topological_sort(graph):
        """Topological sort using DFS"""
        visited = set()
        stack = []
        
        def dfs(vertex):
            visited.add(vertex)
            neighbors = graph.vertices.get(vertex, {}).get('out', [])
            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs(neighbor)
            stack.append(vertex)
        
        for vertex in graph.vertices:
            if vertex not in visited:
                dfs(vertex)
        
        return stack[::-1]
    
    @staticmethod
    def strongly_connected_components(graph):
        """Find SCCs using Kosaraju's algorithm"""
        visited = set()
        stack = []
        
        def dfs1(vertex):
            visited.add(vertex)
            neighbors = graph.vertices.get(vertex, {}).get('out', [])
            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs1(neighbor)
            stack.append(vertex)
        
        for vertex in graph.vertices:
            if vertex not in visited:
                dfs1(vertex)
        
        reverse_graph = {vertex: {'in': graph.vertices[vertex]['out'], 'out': graph.vertices[vertex]['in']} for vertex in graph.vertices}
        
        visited.clear()
        sccs = []
        
        def dfs2(vertex, component):
            visited.add(vertex)
            component.append(vertex)
            neighbors = reverse_graph.get(vertex, {}).get('out', [])
            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs2(neighbor, component)
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                component = []
                dfs2(vertex, component)
                sccs.append(component)
        
        return sccs
