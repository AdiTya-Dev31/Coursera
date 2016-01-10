#! /usr/bin/python

import sys, math, gc

fp = open("trial1.txt")
first_line = fp.readline().split()
num_cities = int(first_line[0])

INF = 2000000
coords = [ [0,0] for _ in range(num_cities)]
dist =  [ [0 for _ in range(num_cities)] for _ in range(num_cities)]

# Now get the x,y co-ordinates
i = 0
for line in fp:
    lst = line.split()
    coords[i][0] = float(lst[0])
    coords[i][1] = float(lst[1])
    i += 1

# compute distances
for i in range(num_cities):
    for j in range(num_cities):
        if(i == j):
            continue
        else:
            # compute euclidean distance between i and j
            x_diff = coords[i][0] - coords[j][0]
            y_diff = coords[i][1] - coords[j][1]
            dist[i][j] = math.sqrt(math.pow(x_diff,2) + math.pow(y_diff,2))

#TSP base case
arr = [ [INF for _ in range(num_cities)] for _ in range(int(math.pow(2,num_cities)))]
arr[1][0] = 0  # Base case where S={1} and j=1 which is 0 in this case

#TSP main loop
for m in range(2,num_cities+1):
    # for each subset of size m that contains 1
    for i in range(int(math.pow(2,m))):
        if i == 0:
            continue
        bini = bin(i)
        if len(bini) == (m+2) and bini[-1] == '1':
            # Innermost loop
            for j in range(1,num_cities):  # j!=city0
                mink = INF
                for k in range(num_cities):
                    if k != j:
                        # S-{j} = i with j removed
                        index = i & ~(1 << j)
                        tmpk = arr[index][k] + dist[k][j]
                        #DEBUG print 'm=%d i=%d bini=%s j=%d k=%d arr[%d][%d]=%d dist[%d][%d]=%d' % (m,i,bini,j,k,index,k,arr[index][k],k,j,dist[k][j])
                        if tmpk < mink:
                            mink = tmpk
                arr[i][j] = mink
        gc.collect()

min_tour = INF
# Return optimal distance
for j in range(1,num_cities):
    ind = int(math.pow(2,num_cities))
    ind -= 1
    #DEBUG print 'j=%d ind=%d arr[ind][j]=%d dist[j][0]=%d' %(j,ind,arr[ind][j],dist[j][0])
    if arr[ind][j] + dist[j][0] < min_tour:
        min_tour = arr[ind][j] + dist[j][0]

print min_tour

