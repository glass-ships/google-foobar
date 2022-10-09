# The Grandest Staircase Of Them All

## Problem 

With the LAMBCHOP doomsday device finished, Commander Lambda is preparing to debut on the galactic stage -- but in order to make a grand entrance, Lambda needs a grand staircase! As the Commander's personal assistant, you've been tasked with figuring out how to build the best staircase EVER. 

Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each amount of bricks, so they can pick the one with the most options. 

Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a height of 1: (# indicates a brick)

```
#
##
21
```

When N = 4, you still only have 1 staircase choice:

```
#
#
##
31
```

But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2), as shown below:

```
#
#
#
##
41
```

```
#
##
##
32
```

Write a function called solution(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!

### Test Cases

solution(200) = 487067745

solution(3) = 1

## Approach 

- see [solution.py](solution.py) for the Python implementation

This turned out to be an example of Euler's distinct partition problem.  
This has a known model, the Partition function Q(n), which gives the number of distinct ways to partition n into unique positive integers.

This one took a while to wrap my head around, and I'm still not happy with my level of understanding.  
But ultimately I was able to implement a solution using some relationships from [Wolfram](https://mathworld.wolfram.com/PartitionFunctionQ.html) and [MSU](https://archive.lib.msu.edu/crcmath/math/math/p/p121.htm)

These are some of the helpful expressions and relations that were involved:  
```python 
Q(n) = coefficient for x**n in G(x)       <- Number of distinct partitions, Q(n)
G(x) = prod(1 + x**k) for k from 0 to n   <- Generating expression for Q(n)
G[k] = G[k-1] * (1 + x**k)                <- generalized iteration
G_k(n) = G_{k-1}(n) + G_k(n-k)            <- Recurrence relation
```

