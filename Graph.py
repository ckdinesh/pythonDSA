class Graph:

    def __init__(self, start, end, routes=[]):
        self.start = start
        self.end = end
        self.paths = []
        self.gdict = {}
        for start, end in routes:
            if start in self.gdict:
                self.gdict[start].append(end)
            else:
                self.gdict[start] = [end]

    def print_dict(self):
        print(self.gdict)

    def print_path(self):
        print(self.paths)

    def get_path(self, start, path=""):

        if self.start == self.end:
            print("Both are same")
            return

        if self.start not in self.gdict:
            print("Staring point not found")
            return

        outer_path = path

        if start in self.gdict:
            for start_node in self.gdict[start]:
                if start_node == self.end:
                    path += "--->" + self.end
                    path = self.start + path
                    self.paths.append(path)
                    path = outer_path
                else:
                    path += "--->" + start_node
                    self.get_path(start_node, path)
                    path = outer_path


if __name__ == '__main__':
    steps = [("Mumbai", "Paris"),
             ("Mumbai", "Dubai"),
             ("Paris", "Dubai"),
             ("Paris", "New York"),
             ("Dubai", "New York"),
             ("New York", "Toronto")]

g = Graph("Dubai", "Toron", steps)
g.print_dict()
g.get_path("Dubai")
g.print_path()
