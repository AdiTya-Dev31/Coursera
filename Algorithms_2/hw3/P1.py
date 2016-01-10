#! /usr/bin/python

import sys
import copy

fp = open("knapsack1.txt")
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
for i in range(1, num_items+2):    # So num_items+1 entries
    temp = [0] * (knapsack_size+1) # So table[i] = [0,1,2,...,knapsack_size]
    table.append(temp)

for i in range(1, num_items+1):
    for j in range(0, knapsack_size+1):
        if weight_array[i] <= j:
            table[i][j] = max(val_array[i]+table[i-1][j-weight_array[i]], table[i-1][j])
        else:
            table[i][j] = table[i-1][j]

#print table
print table[num_items][knapsack_size]
