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

    def dft(self, start_vert):
        to_visit = []
        output = []

        visited = set()

        to_visit.append(start_vert)

        while len(to_visit) > 0:
            current_vert = to_visit.pop()
            # do stuff
            print(current_vert.value)

            # get all connections to visit
            for neighbor in current_vert.get_connections():
                if neighbor not in visited:
                    visited.add(neighbor)

                    to_visit.append(neighbor)

    def dft_p(self, start_vert, target):
        to_visit = []
        visited = set()

        to_visit.append([start_vert])

        while len(to_visit) > 0:
            path = to_visit.pop()

            current_vert = path[-1]
            # do stuff
            if current_vert.value == target:
                return path

            visited.add(current_vert)
            # get all connections to visit
            for neighbor in current_vert.get_connections():
                if neighbor not in visited:
                    visited.add(neighbor)

                    path_copy = path.copy()

                    path_copy.append(neighbor)

                    to_visit.asppend(path_copy)

    def dfs(self, start_vert, target):
        to_visit = []
        output = []

        visited = set()

        to_visit.append(start_vert)

        while len(to_visit) > 0:
            current_vert = to_visit.pop()
            # do stuff
            if current_vert.value == target:
                return current_vert

            # get all connections to visit
            for neighbor in current_vert.get_connections():
                if neighbor not in visited:
                    visited.add(neighbor)

                    to_visit.append(neighbor)
