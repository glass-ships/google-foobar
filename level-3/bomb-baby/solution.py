def solution(M, F):
    """
    Game of Life style problem: 
    Start with the target, subtract the smaller value of the pair from the larger, 
    repeat until base case is reached or found to be impossible.
    """
    step, m, f = 0, int(M), int(F)
    LARGE = 100
    while True:

        # base condition
        if (m <= 0) or (f <= 0)  or (m == f):
            break
        
        # if large target values, reduce to avoid unnecessary computation
        if m > LARGE or f > LARGE:
            if m > f:
                divisor = m//f
                m -= divisor * f
            elif f > m:
                divisor = f//m
                f -= divisor * m
            step += divisor
        
        # otherwise subtract smaller from larger 
        if m > f:
            m -= f
        elif f > m:
            f -= m
        step += 1
    
    # check if we've reached the start of 1 M and 1 F
    if (m == f == 1) and (step >= 0):
        return str(step)
    return 'impossible'
