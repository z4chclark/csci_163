import math

def problem1 (N):
    if (N == 0): return 1
        
    if N % 2 == 0:
        half = problem1(N/2)
        return half * half
    else:
        half = problem1((N-1)/2)
        return 3 * half * half



print(problem1(5))



def problem2 (A):
    
    negatives = []
    positives = []
    zeroes = []

    for num in A:
        if num < 0: negatives.append(num)

        elif num > 0:positives.append(num)

        else: zeroes.append(num)

    return negatives + zeroes + positives

A = [1, -18, 0, -3, 5, -5, 45]
print(problem2(A))