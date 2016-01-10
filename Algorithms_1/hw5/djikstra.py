#! /usr/bin/python

fp= open("dijkstraData.txt")

G = {}
Gdist = {}
NUM_NODES = 200
INF = 80000000

for i in range(1,NUM_NODES+1):
    G[str(i)] = {}
    Gdist[str(i)] = INF # A very large number; ideally infinity

for line in fp: # load data, create adj lists
    lst=[]
    new_list = []
    lst = line.split()
    for elem in lst[1:]:
        # now split the lst to the 2 dictionaries
        new_lst = elem.split(',')
        G[lst[0]][new_lst[0]] = int(new_lst[1])

def find_min(Gdist, unseen_nodes):
    # from the nodes in unseen_nodes, find the min value in Gdist
    minval = INF
    for node in unseen_nodes:
        if Gdist[node] < minval:
            minval = Gdist[node]
            minnode = node
    
    return minnode

def djikstra(start):
    global G, Gdist, INF
    Gdist[start] = 0
    unseen_nodes = G.keys()

    while len(unseen_nodes) > 0:
        # Main loop
        # find the node with the min value in Gdist
        node = find_min(Gdist, unseen_nodes)

        if Gdist[node] == INF:
            break
        unseen_nodes.remove(node)

        # for each neighbor of node, find the smallest weight edge
        for neigh in G[node]:
            dist = Gdist[node] + G[node][neigh] 
            if dist < Gdist[neigh]:
                Gdist[neigh] = dist
                

djikstra('1')
print Gdist['7'],Gdist['37'],Gdist['59'],Gdist['82'],Gdist['99'],Gdist['115'],Gdist['133'],Gdist['165'],Gdist['188'],Gdist['197']

