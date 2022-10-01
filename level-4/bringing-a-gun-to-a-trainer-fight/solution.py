from itertools import product
from math import atan2

def solution(dimensions, your_position, trainer_position, distance):
    """
    Yay, optics problem! Easier to solve on paper, will be a nice challenge to implement into code.

    Snell's Law of Reflection: incoming angle = outgoing angle (assume perfect reflection)
    This means rather than reflecting the beam, we can reflect the room and measure the straight paths. 
    """
    
    beamlen_max = distance
    x0, y0 = your_position
    xf, yf = trainer_position
    
    a = []
    for d in dimensions:
        print(d)
        something = 1 - (distance // -d)
        print(something)
        print(range(something))


    hits = dict()

    # for position in your_position, trainer_position:
    #     print(position)
    #     for reflect in product(*[range(-(distance // -d) + 1) for d in dimensions]):
    #         print(reflect)
    #         for quadrant in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
    #             x, y = [
    #                 (d * r + (d - p if r % 2 else p)) * q
    #                 for d, p, r, q in zip(dimensions, position, reflect, quadrant)
    #             ]
    #             travel = (abs(x - x0) ** 2 + abs(y - y0) ** 2) ** 0.5
    #             bearing = atan2(x0 - x, y0 - y)
    #             if travel > distance or bearing in hits and travel > abs(hits[bearing]):
    #                 continue
    #             # mark self-hits with a negative travel so we can filter later
    #             hits[bearing] = travel * (-1 if position == your_position else 1)
    # return len([1 for travel in hits.values() if travel > 0])


test_cases = [
    ([3,2], [1,1], [2,1], 4),                 # -> 7
    ([300,275], [150,150], [185,100], 500),   # -> 9
]

for dim, your_pos, trainer_pos, dist in test_cases:
    s = solution(dim, your_pos, trainer_pos, dist)
    print('')
    # print(s)