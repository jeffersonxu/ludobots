# ludobots
This contains assignment 8 for Northwestern CS 396: Artifical Life. Specifically, this assignment uses the parallel hill climber to design morphology and behavior for locomotion. The fitness algorithm is the general negative X direction so each creature tries to move in that direction the best it can. The parameters for this evolution is `numberOfGenerations = 20` and `populationSize = 10`. A demonstration of the various creatures generated as well as how they evolve can be seen [here](https://youtu.be/aeAuQopfZxc) and a sample image below. Similar to the previous assignment, my algorithm creates horse like structures with legs on each side similar to the quadraped. A diagram below can be seen how to general structure of the horse is like. This was built using the community [r/ludobots](https://www.reddit.com/r/ludobots/) and depends on [Pyrosim](https://github.com/jbongard/pyrosim). 
![alt text](https://github.com/jeffersonxu/ludobots/blob/assignment7/horse.png)

## Fitness Curves
These were generated using `numpy.random.seed()`

## Diagram
![alt text](https://github.com/jeffersonxu/ludobots/blob/assignment7/diagram.jpg)


## Running
After cloning this repository run the following:
```
pip3 install pybullet numpy
python3 search.py
```
