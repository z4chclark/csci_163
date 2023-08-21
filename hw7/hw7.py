import pdb
import math
import random

def problem1(a, b):
    # Base cases
    if a == 0:
        return 0
    if a < 10:
        return a * b
    
    a_str = str(a)
    b_str = str(b)

    n = len(a_str)
    
    first_half = n//2
    second_half = n - first_half

    a1 = int(a_str[:first_half])
    a2 = int(a_str[first_half:])

    b1 = int(b_str[:first_half])
    b2 = int(b_str[first_half:])

    a3 = a1+a2
    b3 = b1+b2

    p1 = problem1(a1, b1)
    p2 = problem1(a2, b2)
    s = problem1(a3, b3)

    # same as bit shift
    return p1 * (10 ** (2 * second_half)) + (s - p1 - p2) * (10 ** second_half) + p2

a = 2101
b = 1130
print(a*b)
print(problem1(a, b))


def problem2(P):
    
    n = len(P)
    if n == 0 or n == 1:
        return 9999999
    
    mid = (n-1)//2
    median = P[mid]
    Center = []

    delta = min(problem2(P[:mid]), problem2(P[mid+1:]))

    P.sort(key=lambda y: y[1])
    
    for i in range(0, n):
        if abs(P[i][0] - median[0]) <= delta:
            Center.append(P[i])

    for i in range(0, len(Center)):
        for j in range(i+1, min(i+7, len(Center))):
            delta = min(delta, math.sqrt((Center[i][0]-Center[j][0])**2 + (Center[i][1]-Center[j][1])**2))

    return delta

P = []
for i in range(0,5):
    P.append((random.randint(0,9), random.randint(0,9)))

P.sort(key=lambda x: x[0])
print(P)
print(problem2(P)) 


