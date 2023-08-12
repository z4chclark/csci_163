


def hw5(S, k):
    
    #base case
    if (k == 0):
        return [[]] 
    if (not S or len(S) < k):
        return []
    
    first = [S[0]]
    rest = S[1:]
    subsets = []

    subset_with_first = hw5(rest, k-1)
    subset_without_first = hw5(rest, k)

    for subset in subset_with_first:
        subsets.append(first + subset)

    return subsets + subset_without_first


S = ['a','b','c','d']
k = 4

print(hw5(S,k))

