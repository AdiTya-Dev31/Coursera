#! /usr/bin/python

import sys
import copy

fp = open("clustering1.txt")
first_line = fp.readline()
num_nodes = int(first_line)
num_clusters = int(sys.argv[1]) # Given in problem statement
curr_clusters = num_nodes
seen_nodes = []
node_list = []

class Vertex:
    def __init__(self, node, leader=None, size=1):
        self.node = node
        self.leader = self
        self.size = size
        self.children = []
    def __str__(self):
        return "%d with leader %d" %(self.node, self.leader.node)

class Edge:
    def __init__(self, node1, node2, cost, marked=None):
        if node1 not in seen_nodes:
            self.node1 = Vertex(node1)
            seen_nodes.append(node1)
            node_list.append(self.node1)
        else:
            # Find Vertex corresponding to node1 in node_list
            for node in node_list:
                if node.node == node1:
                    self.node1 = node
        if node2 not in seen_nodes:
            self.node2 = Vertex(node2)
            seen_nodes.append(node2)
            node_list.append(self.node2)
        else:
            # Find Vertex corresponding to node1 in node_list
            for node in node_list:
                if node.node == node2:
                    self.node2 = node
        self.cost = cost
        self.marked = marked is not None
    def __str__(self):
        return "%d(leader %d) -> %d(leader %d) with cost %d"% (self.node1.node, self.node1.leader.node, self.node2.node, self.node2.leader.node, self.cost)

def find(vertex):
        return vertex.leader

def union(node1, node2):
    if node2.leader == node1.leader:
        # don't fuse this edge
        return False
    if node2.leader != node1.leader:
        node1.leader.children.append(node2.leader)
        if node2.leader != node2:  # VERY IMPORTANT STEP !
            node2.leader.leader = node1.leader
    #DEBUG: print 'node2 children:'
    for child in node2.leader.children:
        #DEBUG: print child
        child.leader = node1.leader
        node1.leader.children.append(child)

    node2.leader.leader = node1.leader  # VERY IMPORTANT STEP
    #DEBUG print 'node1 children:'
    #DEBUG for child in node1.leader.children:
        #DEBUG print child
    return True

edges = []
for line in fp:
    # initialize the UNdirected graph
    lst = line.split()
    edges.append(Edge(int(lst[0]), int(lst[1]), int(lst[2])) )

# Now sort the graph according to the edges it has
sorted_edges2 = sorted(edges, key=lambda edge: edge.cost)

#for i in range(1, num_nodes - num_clusters+1):
while True:
    # Main loop of clustering/Kruskal's algorithm that runs only
    # up until num_clusters are formed

    # Get min edge
    min_edge = sorted_edges2[0]
    # Merge/Fuse the 2 nodes in this min edge
    #DEBUG print 'fusing edge %s' % min_edge
    if union(min_edge.node1, min_edge.node2):
        curr_clusters -= 1
        if curr_clusters == num_clusters:
            break
    # Remove min_edge from the graph
    sorted_edges2.remove(min_edge)

# remove edges that can cause a cycle
# if this child has an edge to any child of node1.leader
# then remove it
#DEBUG print '--------------------------------------------------------------------------'
for edge in sorted_edges2[:]: # IMPORTANT: iterate over copy of list
    if edge.node1.leader == edge.node2.leader:
        #DEBUG: print 'Possible cycle edge %s' % edge
        sorted_edges2.remove(edge)

#print '--------------------------------------------------------------------------'
min_edge_cost = 50000000
for edge in sorted_edges2:
    if edge.cost < min_edge_cost:
        min_edge_cost = edge.cost

print min_edge_cost
