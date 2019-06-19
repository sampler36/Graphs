"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
      
        self.vertices[vertex] = set()
      
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        pass  # TODO
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        if cb is None:
            def cb(x): return print(x, end=' ')
        visited = set()
        q = Queue()
        q.enqueue(starting_vertex)
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                visited.add(v)
                cb(v)
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)
        print('bft')
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        visited = set()
        s = Stack()
        s.push(starting_vertex)
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print(v, end=' ')
                for neighbor in self.vertices[v]:
                    s.push(neighbor)
        print('dft')

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set()
        q = Queue()
        q.enqueue([starting_vertex])
        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]
            if v == destination_vertex:
                return path
            if v not in visited:
                visited.add(v)
                for neighbor in self.vertices[v]:
                    path_copy = [*path, neighbor]
                    q.enqueue(path_copy)

        raise IndexError(f"bfs {starting_vertex} doesn't connect to {destination_vertex}")                    
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO



class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")
    def dft_r(self, start_vert, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_vert)
        print(start_vert)
        for child_vert in self.vertices[start_vert]:
            if child_vert not in visited:
                self.dft_r(child_vert, visited)

    def dft(self, starting_vertex_id):
        stack = Stack()
        stack.push(starting_vertex_id)
        visited = set()
        while stack.size() > 0:
            v = stack.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vert in self.vertices[v]:
                    stack.push(next_vert)

    def bft(self, starting_vertex_id):
        q = Queue()
        q.enqueue(starting_vertex_id)
        visited = set()
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vert in self.vertices[v]:
                    q.enqueue(next_vert)

    def dfs(self, start_vert, target_value, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_vert)
        if start_vert == target_value:
            return True
        for child_vert in self.vertices[start_vert]:
            if child_vert not in visited:
                if self.dfs(child_vert, target_value, visited):
                    return True
        return False
    def bfs(self, starting_vertex_id, target_value):
        q = Queue()
        q.enqueue(starting_vertex_id)
        visited = set()
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                if v == target_value:
                    return True
                visited.add(v)
                for next_vert in self.vertices[v]:
                    q.enqueue(next_vert)
        return False

    def dfs_r_path(self, start_vert, target_value, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(start_vert)
        path = path + [start_vert]
        if start_vert == target_value:
            return path
        for child_vert in self.vertices[start_vert]:
            if child_vert not in visited:
                new_path = self.dfs_r_path(child_vert, target_value, visited, path)
                if new_path:
                    return new_path
        return None

    def bfs_path(self, starting_vertex_id, target_value):
        q = Queue()
        q.enqueue([starting_vertex_id])
        visited = set()
        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]
            if v not in visited:
                if v == target_value:
                    return path
                visited.add(v)
                for next_vert in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    q.enqueue(new_path)
        return None

    def dfs_path(self, starting_vertex_id, target_value):
        s = Stack()
        s.push([starting_vertex_id])
        visited = set()
        while s.size() > 0:
            path = s.pop()
            v = path[-1]
            if v not in visited:
                if v == target_value:
                    return path
                visited.add(v)
                for next_vert in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    s.push(new_path)
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
