from graph.Graph import Graph, Node, Edge

graph = Graph("../graph1.json")
nodes = graph.get_nodes()
nodes[1].heap_permutation(nodes, len(nodes))
