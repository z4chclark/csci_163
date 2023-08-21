import random

def max_common_intervals(n):
    
    intervals = []
    #assign 1 to start of interval and -1 to end of interval
    for start, end in n:
        intervals.append((start, 1)) 
        intervals.append((end, -1))   
    
    intervals.sort()
    
    max_count = 1
    current_count = 0
    
    #iterate through sorted intervals and add 1 to current_count if start of interval is found and -1 if end of interval is found
    for _, value in intervals:
        current_count += value
        max_count = max(max_count, current_count)
    
    return max_count

n = [(1,4), (0,3), (-1.5,2), (3.6,5)]
print(max_common_intervals(n))

def problem2(arr):

    min_heap = [-num for num in arr]
    heap_sort(min_heap) #using heap_sort from max_heap construction algorithm
    min_heap = [-num for num in min_heap]

    return min_heap

arr = []

for i in range(10):
    arr.append(random.randint(0, 9))

print(problem2(arr))