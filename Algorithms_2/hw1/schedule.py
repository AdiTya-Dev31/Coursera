#! /usr/bin/python

import operator

fp = open("jobs.txt")

num_jobs = int(fp.readline())
jobs = {}
greedy_scores1 = {}
greedy_scores2 = {}

job_id = 1
for line in fp:
    # Load data
    lst = line.split()
    jobs[job_id] = lst
    score1 = int(lst[0]) - int(lst[1])     # score = weight-length
    score2 = float(lst[0])/float(lst[1])   # score = weight/length
    new_lst = []
    new_lst.append(score1)
    new_lst.append(int(lst[0]))
    greedy_scores1[job_id] = new_lst # score,weight
    new_lst = []
    new_lst.append(score2)
    new_lst.append(int(lst[0]))
    greedy_scores2[job_id] = new_lst # score,weight
    job_id += 1

sorted_greed1 = sorted(greedy_scores1.iteritems(), key=operator.itemgetter(1), reverse=True) #using difference
sorted_greed2 = sorted(greedy_scores2.iteritems(), key=operator.itemgetter(1), reverse=True) #using ratio

# Now compute completion time from sorted_greeds
ctime1 = 0
ctime2 = 0
ctime_lst1 = []
ctime_lst2 = []
for i in range(num_jobs):  #iterate num_jobs times
    #ctime1 += sorted_greed1[i][1][1] - sorted_greed1[i][1][0] # weight-score = length
    ctime1 += int(jobs[sorted_greed1[i][0]][1])
    ctime_lst1.append(ctime1)
    ctime2 += int(jobs[sorted_greed2[i][0]][1])
    ctime_lst2.append(ctime2)

wctime1 = 0
wctime2 = 0
for i in range(num_jobs):
    wctime1 += sorted_greed1[i][1][1]*ctime_lst1[i]
    wctime2 += sorted_greed2[i][1][1]*ctime_lst2[i]

print 'greedy difference score completion time = ', wctime1
print 'greedy ratio score completion time = ', wctime2
fp.close()
