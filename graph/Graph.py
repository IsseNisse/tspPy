import json
from Edge import Edge
from Node import Node

graph_file = open("../graph1.json")
lines = json.load(graph_file)

nodes = dict()
edges = dict()

i = 1
j = 1

#
# def get_node_if_exists(node_to_check):
#     for node in nodes:
#         if node_to_check.node_number == nodes[node].node_number:
#             used_node = nodes[node]
#             return used_node
#         else:
#             return False


for line in lines['edges']:
    node1 = Node(line['node1'])
    node2 = Node(line['node2'])

    for node in nodes:
        if node.node_number == node1.node_number:
            from_node = node
        if node.node_number == node2.node_number:
            to_node = node

    if not from_node:
        from_node = node1
        nodes_len = len(nodes)
        nodes[nodes_len + 1] = from_node
    if not to_node:
        to_node = node2

    edge = Edge(node1, node2, line['weight'])
    edges[i] = edge
    i += 1
    j += 2

for node in nodes:
    print(nodes[node].node_number)
