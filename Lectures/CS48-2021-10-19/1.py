class Graph:
    def __init__(self):
        self.vertices = {
                            "A": {"B", "D"},
                            "B": {"C"},
                            "C": {"F"},
                            "D": {"E"},
                            "E": {"G"},
                            "F": {"E"},
                            "G": {},
                        }
                        
                        [
                         [1, 3],
                         [2],
                         [5],
                         [4],
                         [6],
                         [4],
                         []                      
                        ]