# ludobots
This contains assignment 7 for Northwestern CS 396: Artifical Life. Specifically, this assignment builds randomly shaped/sensorized/innervated/motorized "lizards" (2D) and "horses" (3D). My assignment primarily creates horse like structures with legs on each side similar to the quadraped. A diagram below can be seen how to general structure of the horse is like. This was built using the community [r/ludobots](https://www.reddit.com/r/ludobots/) and depends on [Pyrosim](https://github.com/jbongard/pyrosim). As of right now there is no evolution as `numberOfGenerations = 1` and `populationSize = 1` so the horse just sits wiggles a little bit. A demonstration of the various creatures generated can be seen [here](https://youtu.be/aeAuQopfZxc) and a sample image below.

## Diagram
![alt text](https://github.com/jeffersonxu/ludobots/blob/assignment7/diagram.jpg)


## Running
After cloning this repository run the following:
```
pip3 install pybullet numpy
python3 search.py
```
