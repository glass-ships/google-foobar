# Bomb, Baby!

## Problem 

You're so close to destroying the LAMBCHOP doomsday device you can taste it! But in order to do so, you need to deploy special self-replicating bombs designed for you by the brightest scientists on Bunny Planet. There are two types: Mach bombs (M) and Facula bombs (F). The bombs, once released into the LAMBCHOP's inner workings, will automatically deploy to all the strategic points you've identified and destroy them at the same time. 

But there's a few catches. First, the bombs self-replicate via one of two distinct processes: 
Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
Every Facula bomb spontaneously creates a Mach bomb.

For example, if you had 3 Mach bombs and 2 Facula bombs, they could either produce 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs. The replication process can be changed each cycle. 

Second, you need to ensure that you have exactly the right number of Mach and Facula bombs to destroy the LAMBCHOP device. Too few, and the device might survive. Too many, and you might overload the mass capacitors and create a singularity at the heart of the space station - not good! 

And finally, you were only able to smuggle one of each type of bomb - one Mach, one Facula - aboard the ship when you arrived, so that's all you have to start with. (Thus it may be impossible to deploy the bombs to destroy the LAMBCHOP, but that's not going to stop you from trying!) 

You need to know how many replication cycles (generations) it will take to generate the correct amount of bombs to destroy the LAMBCHOP. Write a function solution(M, F) where M and F are the number of Mach and Facula bombs needed. Return the fewest number of generations (as a string) that need to pass before you'll have the exact number of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done! M and F will be string representations of positive integers no larger than 10^50. For example, if M = "2" and F = "1", one generation would need to pass, so the solution would be "1". However, if M = "2" and F = "4", it would not be possible.

### Test Cases

solution('4', '7') = 4
solution('2', '1') = 1


## Approach

- see [solution.py](solution.py) for the Python implementation

This is a neat Game of Life style problem, with the following rules:  
- You start with 1 M and 1 F bomb
- At each generation, either each M bomb spontaneously spawns an F, or vice versa

The goal is to determine how many generations (if even possible) it would take to reach a target number of M and F bombs. 

This could be implemented a number of ways, but I went with a top-down iterative approach.  
Starting with the target numbers of bombs, we know that the greater number of bombs must have been spawned by the lesser number of bombs.  
For example, if at generation i, we have 10 M, 7 F, then we know that in the previous generation, it was the 7 F's which spawned 7 more M's,  
and therefore that at generation i-1, we had 3 M, 7 F.  

A side effect of this fact is that the target M and F *cannot* be the same.  
If for example, the target was 10 M, 10 F, 10-10 = 0 and we know that we start with 1 of each bomb. 

We can also avoid some unnecessary computation with extremely large target values by examining the ratio between the two values and reducing that.  
(Think about the fact that 4500/250 = 90/5)

So the approach is this:  
- Start with the target M, F
- Reduce the values if they're over some user defined threshold 
- Subtract the smaller number from the larger until the target value is foundn to be