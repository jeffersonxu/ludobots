# ludobots
This contains my final project for Northwestern CS 396: Artifical Life. This was built using the community [r/ludobots](https://www.reddit.com/r/ludobots/) and depends on [Pyrosim](https://github.com/jbongard/pyrosim). The fitness function for my robot was to maximize going out of the screen (-x direction). The robot is additionally challenged by a small obstacle course and was evolved using paralell hill climbing.

## Running
After cloning this repository run the following:
```
pip3 install pybullet numpy
python3 search.py
```
