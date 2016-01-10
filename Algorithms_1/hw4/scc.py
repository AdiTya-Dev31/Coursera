#! /usr/bin/python

import sys
import threading
import operator

file= open("SCC.txt")

NUM_NODES = 875714
G = {}
Grev = {}
newG = {}
visited = {}
ftimes = {}
leader = {}
scc_count = {}

time = 0
source = '0'

for i in range(1,NUM_NODES+1):
	G[str(i)] = list()
	Grev[str(i)] = list()
	newG[str(i)] = list()
	visited[str(i)] = 0
	ftimes[str(i)] = 0
	leader[str(i)] = '0'

for line in file: # load data, create adj lists
    lst=[]
    lst = line.split()
    #print lst
    G[lst[0]].append(lst[1])
    Grev[lst[1]].append(lst[0])

def dfs(graph, start):
    global time, visited, ftimes, source, leader
    '''recursive depth first search from start'''
    visited[start] = 1
    leader[start] = source
    for node in graph[start]:
        if visited[node] == 0:
            dfs(graph, node)
    time = time + 1
    ftimes[start] = time

#DFS_loop
def main():
    global source, visited, time, ftimes, leader

    # First DFS lopp pass over Grev
    for i in range(NUM_NODES,0,-1):
        if visited[str(i)] == 0:
            source = str(i)
            dfs(Grev, str(i))

    # Sort nodes by ftimes. Sort the ftimes dict
    sorted_ftimes = sorted(ftimes.iteritems(), key=operator.itemgetter(1), reverse=True)

    # Re-initialize visited array
    for i in range(1,NUM_NODES+1):
        visited[str(i)] = 0
        ftimes[str(i)] = 0
        leader[str(i)] = '0'
    time = 0
    source = '0'

    # Second DFS loop pass over G
    for i in sorted_ftimes:
        if visited[i[0]] == 0:
            source = i[0]
            dfs(G, i[0])

    # Another way to do this by constructing a new graph
    comment='''for i in range(1,NUM_NODES+1):
        for x in G[str(i)]:
            newG[str(ftimes[str(i)])].append(str(ftimes[x]))

    # Re-initialize visited array
    for i in range(1,NUM_NODES+1):
        visited[str(i)] = 0
        ftimes[str(i)] = 0
        leader[str(i)] = '0'
    time = 0
    source = '0'


    for i in range(NUM_NODES,0,-1):
        if visited[str(i)] == 0:
            source = str(i)
            dfs(newG, str(i))'''

    # Now compute the number of nodes that share a single leader
    global scc_count
    for i in leader.itervalues():
        scc_count[i] = scc_count.get(i,0) + 1

    # sort the scc_count dictioary and print the 5 largest scc's
    sorted_scc = sorted(scc_count.iteritems(), key=operator.itemgetter(1))

    print sorted_scc


threading.stack_size(67108864) # 64MB stack
sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
thread = threading.Thread(target = main) # instantiate thread object
thread.start() # run program at target
