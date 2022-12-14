def solution(pegs):
    from fractions import Fraction

    # define an alternating sum for later
    def altsum(l):
        sum = 0
        for i in range(len(l)):
            sum += ((-1)**(i)) * l[i]
        return sum

    # get beamlength, return if 0 or 1
    beamlength = len(pegs)
    if (beamlength <= 1):
        return [-1,-1]

    # check parity and set coefficient, calculate a candidate first gear radius
    isEven = True if (beamlength % 2 == 0) else False
    right_side = pegs[-1] - pegs[0] 
    right_side += 2*(altsum(pegs[1:-1])) if isEven else 2*(altsum(pegs[1:]))
    r_n = float(right_side)/3 if isEven else right_side
    r_0 = Fraction(2*r_n).limit_denominator()
    
    if r_0 < 2:
        return [-1,-1]

    r_curr = r_0
    for i in range(beamlength-2):
        r_next = pegs[i+1] - pegs[i] - r_curr
        if (r_curr < 1) or (r_next < 1):
            return [-1,-1]
        else:
            r_curr = r_next

    return [r_0.numerator, r_0.denominator]
    
test_cases = [
    [4, 30, 50],
    [4, 17, 50],
    [1, 9, 15, 30]
]

for i in test_cases:
    a = solution(i)
    print(a)