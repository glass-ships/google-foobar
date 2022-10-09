def solution(w, h, s):
    """
    Equivalent matrix problem - can be solved using Burnside Lemma
    
    """

    states = [i for i in xrange(0, s-1)]




if __name__ == "__main__":
    test_cases = [
        (2, 2, 2, 7),
        # (2, 3, 4, 430), 
    ]

    for w, h, s, answer in test_cases:
        result = solution(w, h, s)
        # assert result == answer