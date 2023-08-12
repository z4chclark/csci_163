import math

def problem1 (N):
    if (N == 0): return 1
        
    if N % 2 == 0:
        half = problem1(N/2)
        return half * half
    else:
        half = problem1((N-1)/2)
        return 3 * half * half



print(problem1(500000))
