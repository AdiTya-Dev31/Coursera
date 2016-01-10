#! /usr/bin/python

import sys, math, random

fp = open("2sat1.txt")
first_line = fp.readline().split()
num_vars = int(first_line[0])

clauses = [ [0,0] for _ in range(num_vars)]

i = 0
for line in fp:
    lst = line.split()
    clauses[i][0] = int(lst[0])
    clauses[i][1] = int(lst[1])
    i += 1

num_clauses = i

def sol_satisfies_clauses(rand_sol):
    global clauses
    for i in range(num_clauses):
        curr_clause = clauses[i]
        var_a = int(math.fabs(curr_clause[0]))
        var_b = int(math.fabs(curr_clause[1]))
        try:
            val_a = int(rand_sol[var_a])
        except IndexError:
            val_a = 0
        try:         
            val_b = rand_sol[var_b]
        except IndexError:
            val_b = 0
     
        # Evaluate the clause
        if curr_clause[0] < 0:
            val_a = (val_a+1)%2
        if curr_clause[1] < 0:
            val_b = (val_b+1)%2

        if not val_a or val_b:
            return False
    return True

for i in range(1, 1+int(math.log(num_vars,2))):
    # Choose random initial assignment
    rand_sol = random.getrandbits(num_vars)

    for i in range(2*num_vars):
        rand_sol_bin = bin(rand_sol).strip('0b')
        # Check if rand_sol satisfies the list of clauses
        ret = sol_satisfies_clauses(rand_sol_bin)
        if ret == False:
            # Pick random clause
            rand_clause = random.randint(1, num_clauses) 
            # Flip the value of one of its variables, say 0
            flip_var = int(math.fabs(clauses[rand_clause][0]))
            rand_sol &= ~(1 << (num_vars-flip_var))
        else:
            # Returned true, break
            break

    if ret == True:
        print 'Problem solvable'
        break
