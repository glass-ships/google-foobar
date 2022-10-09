# Bringing a Gun to a Trainer Fight

## Problem

Uh-oh -- you've been cornered by one of Commander Lambdas elite bunny trainers!  
Fortunately, you grabbed a beam weapon from an abandoned storeroom while you were running through the station, so you have a chance to fight your way out.  
But the beam weapon is potentially dangerous to you as well as to the bunny trainers: its beams reflect off walls, meaning you'll have to be very careful where you shoot to avoid bouncing a shot toward yourself!  

Luckily, the beams can only travel a certain maximum distance before becoming too weak to cause damage.  
You also know that if a beam hits a corner, it will bounce back in exactly the same direction.  
And of course, if the beam hits either you or the bunny trainer, it will stop immediately (albeit painfully).  

Write a function solution(dimensions, your_position, trainer_position, distance) that takes:
    an array of 2 integers of the width and height of the room,  
    an array of 2 integers of your x and y coordinates in the room,  
    an array of 2 integers of the trainer's x and y coordinates in the room,  
    the maximum distance that the beam can travel;    
and returns an integer of the number of distinct directions that you can fire to hit the elite trainer.

The room has integer dimensions [1 < x_dim <= 1250, 1 < y_dim <= 1250].  
You and the elite trainer are both positioned on the integer lattice at different distinct positions (x, y) inside the room such that [0 < x < x_dim, 0 < y < y_dim].  
Finally, the maximum distance that the beam can travel before becoming harmless will be given as an integer 1 < distance <= 10000.

For example, if you and the elite trainer were positioned in a room with dimensions [3, 2], your_position [1, 1], trainer_position [2, 1], and a maximum shot distance of 4,  
you could shoot in seven different directions to hit the elite trainer (given as vector bearings from your location): [1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], and [-3, -2].  
As specific examples, the shot at bearing [1, 0] is the straight line horizontal shot of distance 1, 
the shot at bearing [-3, -2] bounces off the left wall and then the bottom wall before hitting the elite trainer with a total shot distance of sqrt(13), 
and the shot at bearing [1, 2] bounces off just the top wall before hitting the elite trainer with a total shot distance of sqrt(5).

### Test Cases

solution([3,2], [1,1], [2,1], 4) = 7  

solution([300,275], [150,150], [185,100], 500) = 9

## Approach

- see [solution.py](solution.py) for the Python implementation

Yay, optics problem! As a physicist, this problem brought me a lot of joy to work on.  
Easier to solve on paper, was quite a nice challenge to implement into code.

The physics:
Snell's Law of Reflection tells us that (assuming perfect reflection), when light hits a reflective surface,  `incoming angle = outgoing angle`

This means rather than reflecting the beam, and messing with rotating rooms and keeping track of bouncing around,  
we can easily reflect the room and measure the straight paths. 

The beam also has limited range, so we'll only need a limited number of reflections. 

So the reframed problem becomes - How many direct paths to reflected trainers are there within the range limit of the beam (provided we're not hit along the way!)

To find the number of reflections, we'll need a new room (reflections included) with:  
    `x dimension >= (max beam length + glass's x position),`  
    `y dimenion >= (max beam length + glass's y position).`
    
So, we can re-arrange this relationship a little: 

        `(glass_x + max beam length) <= x_dimension * number of reflections   becomes:`  
        `[number of reflections in x, y] = [int(ceil(glass_pos + beam_range, dimensions))]`

Now we can map out the reflected positions of self and trainer in these reflected spaces, all in the first quadrant of an X-Y coordinate system.  
Then, to allow for a full range of trajectories, we can reflect this new expanded room into quadrants 2, 3, and 4.  
From here, we just coount up direct paths to trainers which are in range of the beam weapon!

The process should look something like: 
- Create a Room in first quadrant of x, y plane and place self and trainer 
- Use beam range to determine how many reflections are needed in x and y
- Create a mapping to these reflection spaces in first quadrant
- Reflect these reflection spaces into quadrants 2-4 to allow for full range of orientations
- Calculate and test all possible beam orientations
- If trainer is hit, add to a total hits counter.  
  If self is hit, that's probably not very good, so we ignore that. 