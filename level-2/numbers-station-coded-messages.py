def solution_recursive(l, t):

    # Assert Bunny HQ standards
    assertions = {
    "List size": (len(l) <= 100) and (len(l) > 1),
    "Element size": (any(i < 100 for i in l) and any(i > 0 for i in l)),
    "Target size": (t>1 and t<250)
    }
    if any(assertions[i] == False for i in assertions):
        raise ValueError("""
-------------------------------------------------------------------------------
Uh oh! Input error - messages must adhere to Bunny HQ standards: 
- List "l" must be between 1 and 100 elements in size.
- Each element of "l" must be between 1 and 100.
- Target value "t" must be a between 1 and 250.
Please check your inputs and try again.
-------------------------------------------------------------------------------
    """)
    
    # Check base conditions
    if l[0] == t:
        print("+ first element is the target")
        return
    elif sum(l) == t:
        print("+ whole list sum is the target")
        return
    elif len(l) == 1:
        print("- target not found in sublist sums")
        return

    target_found = False
    # Process list
    total = 0
    for i in range(len(l)):
        total += l[i]
        print("current value: %d" % l[i])
        print("current total: %d\n" % total)
        if total == t:
            print("target found in sublist sum")
            target_found = True
            break
    
    if target_found:
        # get index of sublist in main list
        return
    # Repeat on next sublist if target is not found in sublist sums
    else:
        solution_recursive(l[1:], t)   

def solution_daniel(l,t):
    a = b = 0
    max = len(l)
    while a < max:
        val = sum(l[a:b+1])
        if val == t:
            return [a, b]
        elif val > t:
            a += 1
            if a > b and b < max:
              b += 1
        elif val < t:
            if b < max:
                b += 1
            else:
                return [-1,-1]
    return [-1,-1]

def solution(l,t):
    
    # Assert Bunny HQ standards
    # assertions = {
    # "List size": (len(l) <= 100) and (len(l) >= 1),
    # "Element size": (any(i < 100 for i in l) and any(i >= 1 for i in l)),
    # "Target size": (t >= 1 and t <= 250),
    # "Int input only": (all(type(i) == int for i in l))
    # }
    # if any(assertions[i] == False for i in assertions):
    #     return [-2,-2]
    if t in l:
        return [l.index(t), l.index(t)]
    sum=0
    start=0
    # start summing up list elements
    for ind, val in enumerate(l):
    
        sum += val
                
        # check we didn't overshoot our target
        while (sum > t and start < ind):
            sum -= l[start]
            start += 1
        
        # if target found, return start and stop indices
        if sum == t:
            return [start,ind]
        # otherwise, sublist sum continues starting at next index

    # if target not found, return -1,-1
    return [-1,-1]

test_cases = [
    ([4, 3, 10, 2, 8], 10),
    ([1, 2, 3, 4], 15),
    ([1, 2, 3, 4], 1),
    ([1, 2, 4, 4], 6),
]

for l, t in test_cases:
    print(solution(l, t))

