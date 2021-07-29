import json
from Edge import Edge
from Node import Node

graph_file = open("../graph1.json")
lines = json.load(graph_file)

nodes = dict()
edges = dict()

i = 1


for line in lines['edges']:
    node1 = Node(line['node1'])
    node2 = Node(line['node2'])
    from_node = None
    to_node = None

    for node_key in nodes:
        if nodes[node_key].node_number == node1.node_number:
            from_node = node_key
        if nodes[node_key].node_number == node2.node_number:
            to_node = node_key

    if not from_node:
        from_node = node1
        nodes_len = len(nodes)
        nodes[nodes_len + 1] = from_node
    if not to_node:
        to_node = node2
        nodes_len = len(nodes)
        nodes[nodes_len + 1] = to_node

    edge = Edge(from_node, to_node, line['weight'])
    edges[i] = edge
    i += 1

# for node_key in nodes:
#     print(nodes[node_key].node_number)
