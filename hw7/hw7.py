import pdb

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