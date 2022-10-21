# Google Foobar

If you're seeing this repository, you're more than likely familiar with the elusive Google Foobar coding challenge.  
Like many others, I was invited at random while performing Python/coding related Google searches.  
Without fully understanding what I was getting involved in, I excitedly agreed and embarked on one of the most exciting journeys of my coding career!  

This repository contains the problems posed, as well as my approaches and solutions.  
My intent is to provide some useful documentation about the types of problems represented, and possible approaches to them.  
If you are invited to Google Foobar, you should make every effort not to copy code you find here, or elsewhere.  
Rather, you should focus on learning as much as you can, and attempt to implement your own solution to the best of your ability.  

When I participated in the challenge (Q3 2022, Foobar version 1-335-gea1c3e3-beta), Python solutions were accepted only in Python 2.7.13.  
As such, many things were implemented slightly differently than they could be now.  
I'm also not an expert by any stretch, so there is likely much room for improvement in both my understanding of and approach to many of these problems.  

## Challenges

### Level 1

- [I Love Lance and Janice](level-1/i-love-lance-and-janice/)

### Level 2

- [Gearing Up For Destruction](level-2/gearing-up-for-destruction/)
- [Numbers Station Coded Messages](level-2/numbers-station-coded-messages/)

### Level 3

- [Bomb Baby](level-3/bomb-baby/)
- [Doomsday Fuel](level-3/doomsday-fuel/)
- [The Grandest Staircase of them All](level-3/the-grandest-staircase-of-them-all/)

### Level 4

- [Bringing a Gun to a Trainer Fight](level-4/bringing-a-gun-to-a-trainer-fight/)
- [Running With Bunnies](level-4/running-with-bunnies/)

### Level 5

- [Disorderly Escape](level-5/disorderly-escape/)

### Post Game

After you complete all 5 levels, you'll get an encrypted message to decode! 
I am by no means an expert on decryption, so I turned to the internet for some help.  
I recommend trying to solve it yourself, but if you're like me and wouldn't know where to start, here's how to approach it.

<details>
  <summary>SPOILERS - decrypting the message</summary>

    First, this should be pretty recognizable as base64, so we `b64decrypt` the initial message to start.  

    This gives us a pretty unrecognizable byte string that we'll need to convert into actual characters.  
    It turns out the coloration on "for YOUR eyes only" is a hint. 
    
    So next, we'll need to decode the byte string using our _username_! 

    The specific way we obtain the target string is where I got stuck:  
    you basically need to iterate through the characters in your username as ASCII characters,  
    cast them as an int using `ord()`, then XOR the result with the corresponding character in the encoded byte string.
  
</details>