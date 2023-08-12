import math

def problem1 (N):
    if (N < 0): return 0
        
    if (N == 0): return 1
        
    if (N == 1): return 3
        
    return problem1(int(N/2)) * problem1(math.ceil(N/2))


print(problem1(5000))