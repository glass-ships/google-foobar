from math import sqrt, atan2

def solution(dimensions, your_position, trainer_position, distance):
    """
    For a room with given dimensions, coordinates for self and trainer, and a max beam range,
    return the number of unique shot trajectories which will hit the trainer but not self.
    """
   
    # Rename some variables for no other reason than to help me keep track 
    dim_x = dimensions[0]
    dim_y = dimensions[1]
    glass_x = your_position[0]
    glass_y = your_position[1]
    trainer_x = trainer_position[0]
    trainer_y = trainer_position[1]
    beam_range = distance

    # add one because python 2 division is a floor by design
    n_reflections_x = int((glass_x + beam_range) / dimensions[0]) + 1 
    n_reflections_y = int((glass_y + beam_range) / dimensions[1]) + 1

    def get_distance(x1, y1, x2, y2):
        return sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

    def get_angle(x1, y1, x2, y2):
        return atan2((y2 - y1), (x2-x1))

    def reflect_point(px, py, rx, ry):
        y = ry*dim_y + (dim_y - py if ry % 2 else py)
        x = rx*dim_x + (dim_x - px if rx % 2 else px)
        return x, y
    
    # get self and trainer positions in first quadrant reflected rooms
    glass = []
    trainer = []
    for rx in xrange(0, n_reflections_x):
        for ry in xrange(0, n_reflections_y):

            if rx == 0 and ry == 0:
                glass.append([glass_x, glass_y])
                trainer.append([trainer_x, trainer_y])
                continue

            glass_r_x, glass_r_y = reflect_point(glass_x, glass_y, rx, ry)
            glass.append([glass_r_x, glass_r_y])

            trainer_r_x, trainer_r_y = reflect_point(trainer_x, trainer_y, rx, ry)
            trainer.append([trainer_r_x, trainer_r_y])
    
    # get self and trainer positions in quadrants 2-4
    glass = glass + [[-x, y] for x, y in glass] + [[-x, -y] for x, y in glass] + [[x, -y] for x, y in glass]
    trainer = trainer + [[-x, y] for x, y in trainer] + [[-x, -y] for x, y in trainer] + [[x, -y] for x, y in trainer]
    corners = [[0, 0], [dimensions[0], 0], [dimensions[0], dimensions[1]], [0, dimensions[1]]]
    
    points_of_interest = [[x, y, 0] for x, y in glass] \
                        + [[x, y, 1] for x, y in trainer] \
                        + [[x, y, 0] for x, y in corners]
    
    # now our possible beam trajectories are the lines from self to each of these points
    # sort by pythagorean distance, filter out entries greater than beam range
    points_of_interest = sorted(points_of_interest, key=lambda x: get_distance(x[0], x[1], glass_x, glass_y))
    points_of_interest = filter(lambda x: get_distance(x[0], x[1], glass_x, glass_y) <= float(beam_range), points_of_interest)
    # print(points_of_interest)

    # rewrite trajectories as angles instead of vectors to remove duplicates (keep shortest paths first)
    angles = {}
    for poi in points_of_interest:
        angle = get_angle(poi[0], poi[1], glass_x, glass_y)
        if angle not in angles:
            angles[angle] = poi

    # count only hits on trainer and not corner or self
    hits = sum(1 for poi in angles.values() if poi[2])
    
    return hits

# Test cases found online
test_cases = [
    ([3, 2], [1, 1], [2, 1], 4, 7), 
    ([10, 10], [4, 4], [3, 3], 5000, 739323), 
    ([2, 5], [1, 2], [1, 4], 11, 27), 
    ([23, 10], [6, 4], [3, 2], 23, 8), 
    ([300, 275], [150, 150], [180, 100], 500, 9), 
    ([1250, 1250], [1000, 1000], [500, 400], 10000, 196), 
]
if __name__ == "__main__":
    for dimension, position, trainer, range, answer in test_cases:
        result = solution(dimension, position, trainer, range)
        assert answer == result