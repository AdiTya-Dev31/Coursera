#! /usr/bin/python

import operator

fp = open("edges.txt")
first_line = fp.readline().split()
num_vertices = int(first_line[0])
num_edges = int(first_line[1])

G = {} # the graph representation as an adjacency list
for i in range(1, num_vertices+1):
    G[i] = []

for line in fp:
    # initialize the UNdirected graph
    lst = line.split()
    G[int(lst[0])].append( (int(lst[1]), int(lst[2])) ) # add v in u's list
    G[int(lst[1])].append( (int(lst[0]), int(lst[2])) ) # add u in v's list

def find_min_edge(G, seen_nodes, unseen_nodes):
    # Choose an edge {u, v} with minimal weight such that u
    # is in seen_nodes and v is in unseen_nodes
    min_weight = 1000000000 # to simulate +INFINITY
    min_node1 = -1
    min_node2 = -1
    for node in seen_nodes:
        # Iterate over adjacency list
        #DEBUG: print 'At node %d' % node
        for adj_node in G[node]:
            #DEBUG: print adj_node
            if adj_node[0] in unseen_nodes:
                # check to see if its weight < min_weight
                if adj_node[1] < min_weight:
                    min_weight = adj_node[1]
                    min_node2 = adj_node[0]  # node2 is from unseen_nodes
                    min_node1 = node         # node1 is from seen_nodes

    if min_node1 == -1:
        # Error; throw exception
        raise Exception('No min edge found across frontier')

    return min_node1, min_node2, min_weight

def primMST(G, start):
    unseen_nodes = G.keys()
    unseen_nodes.remove(start)
    seen_nodes = []
    seen_nodes.append(start)
    mst = []

    while len(unseen_nodes) > 0:
        # Main loop
        node1, node2, weight = find_min_edge(G, seen_nodes, unseen_nodes)
        #DEBUG: print node1, node2, weight
        mst.append( (node1, node2, weight) )
        unseen_nodes.remove(node2)
        seen_nodes.append(node2)

    #DEBUG: print mst
    # compute cost of MST
    cost = 0
    for edge in mst:
        cost += edge[2]

    print 'Cost of Prim\'s MST = %d' % cost

primMST(G, 1)
fp.close()
