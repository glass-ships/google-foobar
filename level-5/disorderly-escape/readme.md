# Disorderly Escape

## Problem

Oh no! You've managed to free the bunny workers and escape Commander Lambdas exploding space station, but Lambda's team of elite starfighters has flanked your ship. If you dont jump to hyperspace, and fast, youll be shot out of the sky!

Problem is, to avoid detection by galactic law enforcement, Commander Lambda planted the space station in the middle of a quasar quantum flux field. In order to make the jump to hyperspace, you need to know the configuration of celestial bodies in the quadrant you plan to jump through. In order to do *that*, you need to figure out how many configurations each quadrant could possibly have, so that you can pick the optimal quadrant through which youll make your jump. 

There's something important to note about quasar quantum flux fields' configurations: when drawn on a star grid, configurations are considered equivalent by grouping rather than by order. That is, for a given set of configurations, if you exchange the position of any two columns or any two rows some number of times, youll find that all of those configurations are equivalent in that way -- in grouping, rather than order.

Write a function solution(w, h, s) that takes 3 integers and returns the number of unique, non-equivalent configurations that can be found on a star grid w blocks wide and h blocks tall where each celestial body has s possible states. Equivalency is defined as above: any two star grids with each celestial body in the same state where the actual order of the rows and columns do not matter (and can thus be freely swapped around). Star grid standardization means that the width and height of the grid will always be between 1 and 12, inclusive. And while there are a variety of celestial bodies in each grid, the number of states of those bodies is between 2 and 20, inclusive. The solution can be over 20 digits long, so return it as a decimal string.  The intermediate values can also be large, so you will likely need to use at least 64-bit integers.

For example, consider w=2, h=2, s=2. We have a 2x2 grid where each celestial body is either in state 0 (for instance, silent) or state 1 (for instance, noisy).  We can examine which grids are equivalent by swapping rows and columns.

00
00

In the above configuration, all celestial bodies are "silent" - that is, they have a state of 0 - so any swap of row or column would keep it in the same state.

00 00 01 10
01 10 00 00

1 celestial body is emitting noise - that is, has a state of 1 - so swapping rows and columns can put it in any of the 4 positions.  All four of the above configurations are equivalent.

00 11
11 00

2 celestial bodies are emitting noise side-by-side.  Swapping columns leaves them unchanged, and swapping rows simply moves them between the top and bottom.  In both, the *groupings* are the same: one row with two bodies in state 0, one row with two bodies in state 1, and two columns with one of each state.

01 10
01 10

2 noisy celestial bodies adjacent vertically. This is symmetric to the side-by-side case, but it is different because there's no way to transpose the grid.

01 10
10 01

2 noisy celestial bodies diagonally.  Both have 2 rows and 2 columns that have one of each state, so they are equivalent to each other.

01 10 11 11
11 11 01 10

3 noisy celestial bodies, similar to the case where only one of four is noisy.

11
11

4 noisy celestial bodies.

There are 7 distinct, non-equivalent grids in total, so solution(2, 2, 2) would return 7.

### Test Cases

solution(2, 3, 4) = 430

solution(2, 2, 2) = 7

## Approach

- see [solution.py](solution.py) for the Python implementation

There's a lot to unpack here so let's start by reducing the problem to one question:  
> *For a matrix of size `h*w`, and `s` possible states for each matrix element,  
how many distinct groupings of permutations are there,  
such that matrices are considered equivalent (symmetric) on row/column swaps?*

One side-effect of row/column swaps is that after any number of swaps, the elements within each row and column are the same (ignoring order).  
So a brute force approach might involve iterating through all possible permutations of a matrix,  
and counting only matrices which can't be row/column shifted to obtain another matrix in the set of solutions.  

This could probably work for small matrices and a small number of states, but for the maximum case, of 20 states in a 12 x 12 matrix,  
we find there are 12*12 choose 20 possible permutations - about 1.5 x 10**24 

So we'll need a more mathematically elegant approach. The wording of the problem suggests that "group theory" and "equivalent matrices" might be good search terms.  
Sure enough, some cursory research brings a few theories to light, namely Burnside's Lemma, Polya Enumeration, and the Cycle Index polynomial.

The Cycle Index polynomial gives a way to enumerate equivalence classes due to a group's action, and is at the heart of both Burnside's Lemma and Polya Enumeration Theorem, so we'll implement this.  
In particular, we'll use the Cycle Index polynomial for the Symmetric Group $S_n$:  
$$Z(S_n) = \sum_{j\in J_n}^{}(\frac{1}{\prod_{k=0}^{n}(k^{j_k}\cdot j_k)}a_{1}^{j_1}a_{2}^{j_2}...a_{p}^{j_p})$$

where $n$ is the size of set.  
We can get the cycle index the columns and rows separately, then combine them for an overall cycle index.  
For each term in the row and column cycle index, the combined contribution can be expressed as:  
$$C(a_{p}^{q}, b_{x}^{y}) = a_{lcm(p,x)}^{p\cdot q\cdot x\cdot y\cdot / lcm(p,x)}$$

**Disclaimer**  
I am by no means an expert on group theory, and unfortunately don't understand the theory behind the math here nearly as well as I'd like to.  
Here are some helpful links to reading which helped me to understand how to approach this problem programmatically:
- https://brilliant.org/wiki/burnsides-lemma/
- https://en.wikipedia.org/wiki/Cycle_index
- https://math.stackexchange.com/questions/2056708/number-of-equivalence-classes-of-w-times-h-matrices-under-switching-rows-and
- https://math.mit.edu/~apost/courses/18.204_2018/Jenny_Jin_paper.pdf

