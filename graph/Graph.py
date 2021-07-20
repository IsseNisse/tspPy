import json
from Edge import Edge
from Node import Node

graph_file = open("../graph1.json")
lines = json.load(graph_file)

nodes = dict()
edges = dict()

i = 1
j = 1


def get_node_if_exists(node_to_check):
    for node in nodes:
        if node_to_check.node_number == nodes[node].node_number:
            used_node = nodes[node]
            return used_node
        else:
            return False


for line in lines['edges']:
    node1 = Node(line['node1'])
    node2 = Node(line['node2'])

    if get_node_if_exists(node1):
        node1 = get_node_if_exists(node1)
    else:
        nodes[j] = node1

    if get_node_if_exists(node2):
        node2 = get_node_if_exists(node2)
    else:
        nodes[j + 1] = node2

    edge = Edge(node1, node2, line['weight'])
    edges[i] = edge
    i += 1
    j += 2

for node in nodes:
    print(nodes[node].node_number)
