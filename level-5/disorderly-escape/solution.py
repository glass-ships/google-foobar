import numpy as np
from fractions import Fraction
from math import factorial

def solution(w, h, s):
    """
    Evaluates the combined cycle index polynomal at s for a matrix of size h x w
    """

    # initialize return value
    num_unique_classes = 0 
    
    # generate cycle index polynomial for row and column sets
    cycle_index_cols = cycle_index(w)
    cycle_index_rows = cycle_index(h)

    # combine cycle indices and (indirectly) count unique classes
    for col_coeff, col_cycle in cycle_index_cols:
        for row_coeff, row_cycle in cycle_index_rows:
            
            # combine coefficients and cycles
            coeff = col_coeff * row_coeff 
            cycle = combine(col_cycle, row_cycle)

            # evaluate polynomial term at s 
            value = 1
            for x, power in cycle:
                value *= s ** power

            # multiply by the coefficient and add to the total
            num_unique_classes += coeff * value
            
    return str(num_unique_classes)

def cycle_index(n):
    """
    Returns a cycle index polynomial in list form:
        [ ( Fraction:{coeff}, [ ( int:{length}, int:{frequency} ):{cycle}, ... ]:{cycles} ):{term}, ... ]
    """
    return [(coeff(term), term) for term in gen_terms(n, n)]

def coeff(term):
    """For a given term in the sum of Z(S_n), calculates the coefficient"""
    denom = 1
    for k, j_k in term:
        denom *= (k**j_k) * factorial(j_k)
    return Fraction(1, denom)

def gen_terms(n, states):
    """
    Generates the disjoint cycle set, J_n, for use in each term of Z(S_n)
    Returns a list_of_solutions[solution[tuple(value, frequency in value)]] 
    For example:
        gen_vars(3, 2) = [
                            [(2, 1), (1, 1)], # 3 = 2*1 + 1*1 
                            [(1, 3)]          # 3 = 1*3
                         ]
    """
    J_n = []
    if n > 0:
        for s in range(states, 0, -1):
            if s == 1:
                J_n.append([(1, n)])
            else: 
                for j in range(int(n/s), 0, -1):
                    recurse = gen_terms(n - s*j, s-1)
                    if len(recurse) == 0:
                        J_n.append([(s, j)])
                    for soln in recurse:
                        J_n.append([(s, j)] + soln)
    return J_n

def combine(term_a, term_b):
    """
    Get the combined contributions of the terms of two cycle index polynomials
    """
    combined = []
    for len_a, freq_a in term_a:
        for len_b, freq_b in term_b:
            lcm = float(np.lcm(len_a, len_b))
            combined.append((lcm, int(len_a * freq_a * len_b * freq_b / lcm)))
    return combined


###   Testing   ###
if __name__ == "__main__":
    test_cases = [
        (2, 2, 2, '7'),
        (2, 3, 4, '430'), 
        (12, 12, 20, '97195340925396730736950973830781340249131679073592360856141700148734207997877978005419735822878768821088343977969209139721682171487959967012286474628978470487193051591840')
    ]

    for w, h, s, answer in test_cases:
        result = solution(w, h, s)
        # print(f"\nExpected:\n{answer}\n\nCalculated:\n{result}")
        print("")
        print("Expected: {}".format(answer))
        print("")
        print("Calculated: {}".format(result))
        
        assert result == answer