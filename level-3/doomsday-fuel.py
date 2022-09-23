def solution(m):
    """
    For a given matrix, m, which represents an absorbing markov chain, 
    return a list of probabilities for each terminal state plus the denominator 
    Markov chain absorption problem:
    0. Identify absorbing states (0 chance to enter any other state, probability 1 to re-enter current state)
    1. "minimize" matrix, from total to fraction of total, add 1 for P[i][i] entries in absorbing states
    2. get matrices R and Q
    3. get matrix FR
    4. ????
    """
    import numpy as np
    from fractions import Fraction
    
    m = np.array(m)
    ### Helper methods ###
    def _fraction(num, dem):
        return 0 if num == 0 else Fraction(num, dem)

    def _identity(n):
        "Return identity matrix of given size"
        return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    def _get_transition_matrix(m, absorbing_states, transition_states):
        """
        Returns almost canonical transform matrix:
        Q R              I 0
        0 I  instead of  R Q
        """
        # get modified transition matrix
        M = []
        for s, probs in enumerate(m):
            row = []
            for s_next, p_next in enumerate(probs):
                row.append(
                    1 if (s in absorbing_states and s == s_next) else _fraction(p_next, sum(m[s]))
                    # 1 if (s in absorbing_states and s == s_next) else p_next
                )
            M.append(row)
        
        # re-arrange into canonical form
        P = np.array(M)
        P = P[:, absorbing_states+transition_states]
        P = P[absorbing_states+transition_states, :]
        return P

    ### Main solution ###
    
    # 0. get (indexes for) absorbing and transient states
    transition_states = [] # [0, 1]
    absorbing_states = [] # [2, 3, 4, 5]
    for i in range(len(m)):
        row = m[i]
        if sum(row) == 0:
            absorbing_states.append(i)
        elif sum(row) == 1 and m[i, i] == 1:
            absorbing_states.append(i)
        else:
            transition_states.append(i)
    
    # If only 1 absorbing state, return 100% chance to absorb
    if len(absorbing_states) == 1:
        return [1, 1]
    
    # 1. get (non-canonical) transition matrix
    P = _get_transition_matrix(m, absorbing_states, transition_states)

    # 2. get matrices R and Q
    R = P[len(absorbing_states):, :len(absorbing_states)]
    Q = P[len(absorbing_states):, len(absorbing_states):]
    

    # 3. get matrix FR
    I = _identity(len(Q))
    diff = (I-Q).astype(np.float)
    F = np.linalg.inv(diff)
    F = [ [Fraction(F[i][j]).limit_denominator() for j in range(len(F[i]))] for i in range(len(F))]
    FR = np.matmul(F, R)

    # 4. Express first row of FR in terms of least common denominator
    probabilities = FR[0]
    lcm = np.lcm.reduce([p.denominator for p in probabilities])
    result = [p.numerator * lcm // p.denominator for p in probabilities]
    result.append(lcm)
    # print("\nTransition states: {}".format(transition_states))
    # print("Absorbing states: {}".format(absorbing_states))
    # print("\nCanonical transition matrix: \n{}\n".format(P))
    # print("\nMatrix R:\n{}\n".format(R))
    # print("\nMatrix Q:\n{}\n".format(Q))
    # print("\nProbability matrix: {}\n".format(probabilities))
    # print("Result:\n{}".format(result))
    return result

# Testing
test_cases = [
    [[0, 2, 1, 0, 0],
    [0, 0, 0, 3, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0,0],
    [0, 0, 0, 0, 0]], # -> [7, 6, 8, 21]
    
    [[0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]] # -> [0, 3, 2, 9, 14]
]

for m in test_cases:
    result = solution(m)
    print(result)
