import json


class Node:
    def __init__(self, node_number):
        self.node_number = node_number

    def heap_permutation(self, a, size, first_node):
        # print('size ' + str(size))
        # if size becomes 1 then prints the obtained
        # permutation
        if size == 1:
            for key in a:
                print(a[key].node_number)
            print(a)
            return

        for i in range(size):
            self.heap_permutation(a, size - 1, first_node)

            # if size is odd, swap 0th i.e (first)
            # and (size-1)th i.e (last) element
            # else If size is even, swap ith
            # and (size-1)th i.e (last) element
            if size & 1:
                a[first_node], a[size + first_node - 1] = a[size + first_node - 1], a[first_node]
            else:
                a[i + first_node], a[size + first_node - 1] = a[size + first_node - 1], a[i + first_node]


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
        edges = dict()

        i = 1

        for line in lines['edges']:
            node1 = Node(line['node1'])
            node2 = Node(line['node2'])
            from_node = None
            to_node = None

            for node_key in self.nodes:
                if self.nodes[node_key].node_number == node1.node_number:
                    from_node = node_key
                if self.nodes[node_key].node_number == node2.node_number:
                    to_node = node_key

            if not from_node:
                from_node = node1
                nodes_len = len(self.nodes)
                self.nodes[nodes_len + 1] = from_node
            if not to_node:
                to_node = node2
                nodes_len = len(self.nodes)
                self.nodes[nodes_len + 1] = to_node

            edge = Edge(from_node, to_node, line['weight'])
            edges[i] = edge
            i += 1

    def get_nodes(self):
        return self.nodes

# for node_key in nodes:
#     print(nodes[node_key].node_number)
