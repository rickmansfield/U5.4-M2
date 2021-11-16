class Vertex:
    def __init__(self, value):
        self.value = value
        self.connections = {}

    def __str__(self):
        return str(self.value) + ' connections: ' + str([x.value for x in self.connections])

    def add_connection(self, vert, weight=0):
        self.connections[vert] = weight

    def get_connections(self):
        return self.connections.keys()

    def get_value(self):
        return self.value

    def get_weight(self, vert):
        return self.connections[vert]


class Graph:
    def __init__(self):
        self.vertices = {}
        self.count = 0

    def __contains__(self, vert):
        return vert in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, value):
        self.count += 1
        new_vert = Vertex(value)
        self.vertices[value] = new_vert
        return new_vert

    def add_edge(self, v1, v2, weight=0):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        self.vertices[v1].add_connection(self.vertices[v2], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def depth_first_search(self, starting_node):
        # stack to visit
        to_visit = []
        # visited set
        visited = set()
        # push the starting node
        to_visit.append(starting_node)
        # add the starting node to the visited set
        visited.add(starting_node)
        # while the stack is not empty
        while len(to_visit) > 0:
            # pop the current node
            current_node = to_visit.pop()

            # visit all neighbors of the current node
            for neighbor in current_node.get_connections():
                # if the neighbor is not in the visited set
                if neighbor not in visited:
                    # add the neighbor to visited
                    visited.add(neighbor)
                    # push the neighbor
                    to_visit.append(neighbor)

    def depth_first_search_r(self, vertex, visited=set()):
        # add the vertex to the visited set
        visited.add(vertex)
        # visit all of the neighbors
        for neighbor in vertx.get_connections():
            # if neighbor is not in the visited set
            if neighbor not in visited:
                # call dfs recursively pass the neighbor and the visited set
                self.depth_first_search_r(neighbor, visited)
