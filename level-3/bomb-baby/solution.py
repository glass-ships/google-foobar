def solution(M, F):
    step, m, f = 0, int(M), int(F)
    LARGE = 100
    while True:
        # base condition
        if (m <= 0) or (f <= 0)  or (m == f):
            break
        if m > LARGE or f > LARGE:
            if m > f:
                divisor = m//f
                m -= divisor * f
            elif f > m:
                divisor = f//m
                f -= divisor * m
            step += divisor
        if m > f:
            m -= f
        elif f > m:
            f -= m
        step += 1
        
    if (m == f == 1) and (step >= 0):
        return str(step)
    return 'impossible'

print(solution(4, 7))
print(solution(2, 1))
print(solution(5, 5))
print(solution(2014, 21))
print(solution(2014, 22))