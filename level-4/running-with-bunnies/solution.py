from copy import deepcopy
from itertools import permutations

def floydWarshall(M):
    """
    Given an adjacency matrix M, returns a new matrix of shortest distances from each node to each other node
    """    
    n = len(M)
    sp = deepcopy(M)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                sp[i][j] = min(sp[i][j], sp[i][k] + sp[k][j])
    return sp

def solution(times, time_limit):
    """
    Input is a graph with weighted edges and potential negative cycles;
    Floyd Warshall algorithm should work here

    Solved with the help of code and documentation from:
        github: n3a9
        github: ken-power

    Arguments:
        times: List(List()) -       Adjacency matrix for starting room, bulkhead, and up to 5 bunnies
        time_limit: int     -       Time before bulkhead closes 
    """

    # assure input is within parameters of problem
    if len(times) != len(times[0]) or (time_limit not in range(1000)):
        return []
    
    # Perform Floyd-Warshall algorithm on times matrix 
    sp = floydWarshall(times)

    ### Start saving bunnies
    
    n = len(times)
    n_bunnies = n - 2
    bunnies = [ i for i in range(n_bunnies)]
    bunnies_saved = []

    # Check for negative cycles, save all bunnies
    for i in range(n):
        if sp[i][i] < 0:
            return bunnies

    # Check for shortest paths which save the most bunnies
    # (brute-force by permuting all possible paths from longest to shorted, and grabbing the first that works or [] if none)
    for i in reversed(range(n_bunnies+1)):
        for permutation in permutations(iterable=range(1, n_bunnies+1), r=i):
            time = 0
            
            # construct a path through rooms based on permutation
            rooms = [0] + list(permutation) + [-1]
            path = []
            for i in range(1, len(rooms)):
                path.append((rooms[i - 1], rooms[i]))
            
            # count total time for path
            for start, end in path:
                time += sp[start][end]
            
            # if total path takes less than time limit, return longest sorted 
            if time <= time_limit:
                bunnies_saved = sorted(list(i-1 for i in permutation))
                return bunnies_saved
    
    return bunnies_saved





########### TESTING ###########

if __name__ == '__main__':
    case1 = [[0, 1, 1, 1, 1],
             [1, 0, 1, 1, 1],
             [1, 1, 0, 1, 1],
             [1, 1, 1, 0, 1],
             [1, 1, 1, 1, 0]]
    print("\n\nCase 1: Provided test case 1.\nTime limit: 3")
    for row in case1:
        print('', row)
    print("\n  Expected: [0, 1]\nCalculated:", str(solution(case1, 3)))

    print("\n\nCase 2: Provided test case 2.\nTime limit: 1")
    case2 = [[0, 2, 2, 2, -1],
             [9, 0, 2, 2, -1],
             [9, 3, 0, 2, -1],
             [9, 3, 2, 0, -1],
             [9, 3, 2, 2, 0]]
    for row in case2:
        print('', row)
    print("\n  Expected: [1, 2]\nCalculated:", str(solution(case2, 1)))

    print("\n\nCase 3: Infinite negative cycle.\nTime limit: -500")
    case3 = [[0, 2, 2, 2, -1],
             [9, 0, 2, 2, 0],
             [9, 3, 0, 2, 0],
             [9, 3, 2, 0, 0],
             [-1, 3, 2, 2, 0]]
    for row in case3:
        print('', row)
    print("\n  Expected: [0, 1, 2]\nCalculated:", str(solution(case3, -500)))

    print("\n\nCase 4: Max bunnies. None rescuable.\nTime limit: 1")
    case4 = [[1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1]]
    for row in case4:
        print('', row)
    print("\n  Expected: []\nCalculated:", str(solution(case4, 1)))

    print("\n\nCase 5: One bunny.\nTime limit: 2")
    case5 = [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]
    for row in case5:
        print('', row)
    print("\n  Expected: [0]\nCalculated:", str(solution(case5, 2)))

    print("\n\nCase 6: Multiple revisits.\nTime limit: 10")
    case6 = [[0, 5, 11, 11, 1],
             [10, 0, 1, 5, 1],
             [10, 1, 0, 4, 0],
             [10, 1, 5, 0, 1],
             [10, 10, 10, 10, 0]]
    for row in case6:
        print('', row)
    print("\n  Expected: [0, 1]\nCalculated:", str(solution(case6, 10)))

    print("\n\nCase 7: Multiple Revisits 2.\nTime limit: 5")
    case7 = [[0, 10, 10, 10, 1],
             [0, 0, 10, 10, 10],
             [0, 10, 0, 10, 10],
             [0, 10, 10, 0, 10],
             [1, 1, 1, 1, 0]]
    for row in case7:
        print('', row)
    print("\n  Expected: [0, 1]\nCalculated:", str(solution(case7, 5)))

    print("\n\nCase 8: Time travel.\nTime limit: 1")
    case8 = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
    for row in case8:
        print('', row)
    print("\n  Expected: [0, 1, 2]\nCalculated:", str(solution(case8, 1)))

    print("\n\nCase 9: No bunnies.\nTime limit: 1")
    case9 = [[2, 2],
             [2, 2]]
    for row in case9:
        print('', row)
    print("\n  Expected: []\nCalculated:", str(solution(case9, 1)))

    print("\n\nCase 10: Backwards bunny path.\nTime limit: 6")
    case10 = [[0, 10, 10, 1, 10],
              [10, 0, 10, 10, 1],
              [10, 1, 0, 10, 10],
              [10, 10, 1, 0, 10],
              [1, 10, 10, 10, 0]]
    for row in case10:
        print('', row)
    print("\n  Expected: [0, 1, 2]\nCalculated:", str(solution(case10, 6)))