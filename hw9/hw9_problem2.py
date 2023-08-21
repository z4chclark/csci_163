
# simple implementation of the Longest Processing Time First (LPT) algorithm for two-processor scheduling
def problem2 (jobs):

    jobs.sort(reverse=True)
    
    processor1 = []
    processor2 = []

    for job in jobs:
        if sum(processor1) < sum(processor2):
            processor1.append(job)
        else:
            processor2.append(job)

    return processor1, processor2


jobs = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

processor1, processor2 = problem2(jobs)

# The time spent by one job in the system is the sum of the time spent by this job in waiting plus the time spent on its execution
#calculate the total time spent by each processor
print("Total time spent by processor 1: " + str(sum(processor1)))
print("Total time spent by processor 2: " + str(sum(processor2)))
