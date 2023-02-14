# ludobots
This contains assignment 6 for Northwestern CS 396: Artifical Life. Specifically, this assignment builds a kinematic chain (a jointed, motorized, innervated, sensorized snake). This was built using the community [r/ludobots](https://www.reddit.com/r/ludobots/) and depends on [Pyrosim](https://github.com/jbongard/pyrosim). As of right now there is no evolution as `numberOfGenerations = 1` and `populationSize = 1` so the snake just sits there and wigles a little bit. A demonstration of the various creatures generated can be seen [here](https://youtu.be/tbStfZbY8Co).

## Running
After cloning this repository run the following:
```
pip3 install pybullet numpy
python3 search.py
```
