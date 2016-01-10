#! /usr/bin/python

fp= open("2sum.txt")

NUM_INTS = 0
htable = {}
array = []
count = 0

for line in fp: # load data
    NUM_INTS = NUM_INTS + 1
    htable[line.strip()] = int(line)
    array.append(int(line))

for t in range(2500,4501):
    acopy = array[:]
    for j in range(0,NUM_INTS):
        # check if there is i-array[j] in the htable
        #print i,array[j]
        if (t-acopy[j]) < 1:
            continue
        else:
            if str(t-acopy[j]) in htable:
                #print i, array[j], htable[str(i-array[j])]
                acopy.remove(t-acopy[j])
                count = count + 1

print count
