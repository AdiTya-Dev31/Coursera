#! /usr/bin/python

import sys

fp = open("g3.txt")
first_line = fp.readline().split()
num_vertices = int(first_line[0])
num_edges = int(first_line[1])

INF=200000000

# From wikipedia pseudocode
dist =  [ [INF for _ in range(num_vertices)] for _ in range(num_vertices)]
for i in range(num_vertices):
    dist[i][i] = 0

for line in fp:
    lst = line.split()
    dist[int(lst[0]) -1][int(lst[1]) -1] = int(lst[2]) # The -1 because lst indices range from 0->num_vertices-1

for k in range(num_vertices):
    for j in range(num_vertices):
        for i in range(num_vertices):
            if(dist[i][k] + dist[k][j] < dist[i][j]):
                dist[i][j] = dist[i][k] + dist[k][j]

# Detect if there are any negative cycles
for i in range(num_vertices):
    if (dist[i][i] < 0):
        print 'Negative cycle exists in graph from node %d' % (i+1)
        sys.exit(0)

# Else detect the shortest path
shortest_i = -1
shortest_j = -1
shortest_plen = INF
for i in range(num_vertices):
    for j in range(num_vertices):
        if (dist[i][j] < shortest_plen):
            shortest_plen = dist[i][j]
            shortest_i = i
            shortest_j = j

print 'Shortest path is from %d to %d with len %d' %( (shortest_i+1),(shortest_j+1), shortest_plen)
