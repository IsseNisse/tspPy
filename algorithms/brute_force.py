from graph.Graph import Graph, Node, Edge

graph = Graph("../graph1.json")
nodes = graph.get_nodes()
heap_nodes = nodes.copy()
del heap_nodes[1]
first_node = list(heap_nodes.keys())[0]
all_paths = nodes[first_node].heap_permutation(heap_nodes, len(heap_nodes), first_node)
print(all_paths)
