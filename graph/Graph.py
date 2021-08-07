import json


class Node:
    def __init__(self, node_number):
        self.node_number = node_number
        self.path = dict()
        self.edges = dict()
        self.i = 1

    def heap_permutation(self, a, size, first_node):

        if size == 1:
            a_copy = a.copy()
            self.path['dict' + str(self.i)] = a_copy
            self.i += 1
            return

        for i in range(size):
            self.heap_permutation(a, size - 1, first_node)

            if size & 1:
                a[first_node], a[size + first_node - 1] = a[size + first_node - 1], a[first_node]
            else:
                a[i + first_node], a[size + first_node - 1] = a[size + first_node - 1], a[i + first_node]
        return self.path

    def add_edge(self, edge, i):
        self.edges[i] = edge

    def get_edge(self, node):
        edge_return = None
        for edge_key in self.edges:
            edge = self.edges[edge_key]
            if edge.node1 == node:
                edge_return = edge
            elif edge.node2 == node:
                edge_return = edge
        return edge_return


class Edge:
    def __init__(self, node_a, node_b, weight):
        self.node1 = node_a
        self.node2 = node_b
        self.weight = weight


class Graph:
    def __init__(self, file):
        self.file = file
        self._make_graph(file)

    def _make_graph(self, file):
        try:
            graph_file = open(file)
        except FileNotFoundError:
            raise FileNotFoundError

        lines = json.load(graph_file)

        self.nodes = dict()
        self.edges = dict()

        i = 1

        for line in lines['edges']:
            node1 = Node(line['node1'])
            node2 = Node(line['node2'])
            from_node = None
            to_node = None

            for node_key in self.nodes:
                if self.nodes[node_key].node_number == node1.node_number:
                    from_node = self.nodes[node_key]
                if self.nodes[node_key].node_number == node2.node_number:
                    to_node = self.nodes[node_key]

            if not from_node:
                from_node = node1
                nodes_len = len(self.nodes)
                self.nodes[nodes_len + 1] = from_node
            if not to_node:
                to_node = node2
                nodes_len = len(self.nodes)
                self.nodes[nodes_len + 1] = to_node

            edge = Edge(from_node, to_node, line['weight'])
            from_node.add_edge(edge, i)
            to_node.add_edge(edge, i)
            self.edges[i] = edge
            i += 1

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

# for node_key in nodes:
#     print(nodes[node_key].node_number)
