#! /usr/bin/python

import sys
import copy

fp = open("clustering2.txt")
first_line = fp.readline().split()
num_nodes = int(first_line[0])
num_bits = int(first_line[1])
max_spacing_in_cluster = int(sys.argv[1]) # Given in problem statement
seen_nodes = []
node_list = []

class Vertex:
    def __init__(self, node_num, hamming_list, leader=None, size=1):
        self.node = node_num
        self.hamming_list = hamming_list
        hamming_weight = 0
        for bit in hamming_list:
            hamming_weight += int(bit)
        self.hamming_weight = hamming_weight
        self.leader = self
        self.size = size
        self.children = []
    def __str__(self):
        return "%d with leader %d with weight %d" % (self.node, self.leader.node, self.hamming_weight)

class Edge:
    def __init__(self, node1, node2, cost, marked=None):
        self.node1 = node1
        self.node2 = node2
        self.cost = cost
        self.marked = marked
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

def hamming_distance(node1, node2):
    # HW between node1 and node2
    dist = 0
    for bit in range(0,num_bits):
        dist += abs( int(node1.hamming_list[bit]) - int(node2.hamming_list[bit]) )
    return dist 

hamming_sets = {}
for i in range(0, 25): # 0-> 24
    hamming_sets[i] = []

nodes = []
node_num = 1
for line in fp:
    # initialize the UNdirected graph
    lst = line.split()
    new_node = Vertex(node_num, lst)
    nodes.append(new_node )
    node_num += 1
    hamming_sets[new_node.hamming_weight].append(new_node)


# For each set in the hamming_sets, compute the hamming distances in the 
# same bucket and bucket-1, bucket-2,... bucket-max_spacing_in_cluster
# and in bucket+1, bucket+2...,bucket+max_spacing_in_cluster
edges = []

num_edges = 0
for i in range(0, num_bits):
    if hamming_sets[i] != []:
        for node1 in hamming_sets[i]:
            for j in range(i-max_spacing_in_cluster, i+max_spacing_in_cluster+1):
                if j < 0 or j > num_bits:
                    continue
                if hamming_sets[j] != []:
                    for node2 in hamming_sets[j]:
                        if node2 != node1 and node2 not in seen_nodes:
                            # Get distance with other nodes in same set
                            dist = hamming_distance(node1, node2)
                            if dist <= max_spacing_in_cluster:
                                seen_nodes.append(node1)
                                edges.append(Edge(node1, node2, dist) )
                                num_edges += 1
    else:
        continue


comment = '''
for node1 in nodes:
    for node2 in nodes:
        if node1 != node2 and node2 not in seen_nodes:
            dist = hamming_distance(node1, node2)
            if dist <= max_spacing_in_cluster:
                seen_nodes.append(node1)
                edges.append(Edge(node1, node2, dist) )
                num_edges += 1'''

# Now sort the graph according to the edges it has
sorted_edges = sorted(edges, key=lambda edge: edge.cost)

print '-------------------------------------------------------------------'
curr_clusters = num_nodes
for i in range(1, num_edges+1):
    # Main loop of clustering/Kruskal's algorithm that runs only
    # up until num_clusters are formed

    # Get min edge
    min_edge = sorted_edges[0]
    # Merge/Fuse the 2 nodes in this min edge
    #DEBUG print 'fusing edge %s' % min_edge
    if union(min_edge.node1, min_edge.node2):
        curr_clusters -= 1
    # Remove min_edge from the graph
    sorted_edges.remove(min_edge)

print curr_clusters

