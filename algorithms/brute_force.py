from graph.Graph import Graph, Node, Edge

graph = Graph("../graph1.json")
nodes = graph.get_nodes()
heap_nodes = nodes.copy()
first_node = heap_nodes[1]
first_node_key = list(nodes.keys())[0]
del heap_nodes[1]
heap_first_node = list(heap_nodes.keys())[0]
paths = nodes[heap_first_node].heap_permutation(heap_nodes, len(heap_nodes), heap_first_node)
shortest_weight = 0
shortest_path = None

for path_key in paths:
    path = paths[path_key]
    path[first_node_key] = first_node
    edges = []
    total_w = 0
    for node_key in path:
        if node_key < len(path) - 1:
            edge = path[node_key].get_edge(path[node_key + 1])
            edges.append(edge)
        else:
            edge = path[node_key].get_edge(path[first_node_key])
            edges.append(edge)
    for edge in edges:
        total_w += edge.weight
        print(edge.weight)

    print('total: ' + str(total_w) + '\n')

    if shortest_weight == 0 or total_w < shortest_weight:
        shortest_weight = total_w
        shortest_path = path


# print(shortest_weight)
print(str(shortest_path[1].node_number) + '' + str(shortest_path[2].node_number) + '' + str(shortest_path[3].node_number) + '' + str(shortest_path[4].node_number) + '' + str(shortest_path[5].node_number))

