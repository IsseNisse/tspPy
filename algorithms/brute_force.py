from graph.Graph import Graph, Node, Edge

graph = Graph("../graph1.json")
nodes = graph.get_nodes()
heap_nodes = nodes.copy()
first_node = heap_nodes[1]
first_node_key = list(nodes.keys())[0]
del heap_nodes[1]
heap_first_node = list(heap_nodes.keys())[0]
paths = nodes[heap_first_node].heap_permutation(heap_nodes, len(heap_nodes), heap_first_node)

for path_key in paths:
    path = paths[path_key]
    path[first_node_key] = first_node
    for node_key in path:
        if node_key == len(path) - 1:
            edge = path[node_key].get_edge(path[node_key + 1])
            print(edge)

