def solution(n):
    """
    Partition function F
    For a given positive integer n, 
    Return Q(n) - the number of distinct ways to partition n into unique positive integers
    """

    # Q(n) = coefficient for x^n in G(x)       <- Number of distinct partitions, Q(n)
    # G(x) = prod(1 + x^k) for k from 0 to n   <- Generating expression for Q(n)
    # G[k] = G[k-1] * (1 + x^k)                <- generalized iteration
    # G_k(n) = G_{k-1}(n) + G_k(n-k)           <- Recurrence relation
    import numpy as np

    G = np.empty([n, n+1])
    G[0] = [int(degree == 0) for degree in range(n+1)]
    
    #print("\nInitial coefficients: {}".format(G[0]))
    for k in range(1, n):
        for i in range(n+1):
            G[k][i] = G[k-1][i] if (k > i) else (G[k-1][i] + G[k-1][i-k])
    return int(G[-1][-1])

def solution_alt(n):

    G = [int(degree == 0) for degree in range(n+1)]
    print("\nInitial coefficients: {}".format(G))
    for k in range(1, n):
        for i in range(n+1):
            G = [ G[i] if (k > i) else G[i] + G[i-k] for i in range(n+1) ]
    return G[n]