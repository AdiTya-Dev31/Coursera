#! /usr/bin/python

import sys
import copy

fp = open("P1_trial1.txt")
first_line = fp.readline().split()
knapsack_size = int(first_line[0])
num_items = int(first_line[1])

val_array = []
weight_array = []
val_array.append(0)
weight_array.append(0)
for line in fp:
    lst = line.split()
    val_array.append(int(lst[0]))
    weight_array.append(int(lst[1]))

table = []
for i in range(0, 2):    # So num_items+1 entries
    temp = [0] * (knapsack_size+1) # So table[i] = [0,1,2,...,knapsack_size]
    table.append(temp)

for i in range(1, num_items+1):
    table[0] = table[1]
    table[1] = temp
    print table
    for j in range(0, knapsack_size+1):
        if weight_array[i] <= j:
            table[1][j] = max(val_array[i]+table[0][j-weight_array[i]], table[0][j])
        else:
            table[1][j] = table[0][j]
    # throw away table[0] and set it to table[1]
    #table[0] = table[1]
    #table.pop(0)
    # reset table[1]
    #table.append(temp)
    #table[1] = temp
    #for j in range(0, knapsack_size+1):
    #    table[0][j] = table[1][j]
    #    table[1][j] = 0
    #print table

#print table
print table[0][knapsack_size]
print table[1][knapsack_size]
