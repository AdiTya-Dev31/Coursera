#! /usr/bin/python

fp= open("Median.txt")

NUM_INTS = 0
array = []
median_array = []
summ = 0

for line in fp: # load data
    NUM_INTS = NUM_INTS + 1
    array.append(int(line))
    median_array.append(0)

for k in range(0,NUM_INTS):
    # compute median
    sorted_array = array[0:k+1]
    sorted_array.sort()
    if k%2 == 0:
        median_array[k] = sorted_array[(k+1)/2]
    else:
        median_array[k] = sorted_array[k/2]

for i in range(0,NUM_INTS):
    # compute sum
    summ = summ + median_array[i]

print summ
print summ%NUM_INTS
