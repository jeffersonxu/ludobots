# ludobots
This contains assignment 8 for Northwestern CS 396: Artifical Life. Specifically, this assignment uses the parallel hill climber to design morphology and behavior for locomotion. The fitness algorithm is the general negative X direction so each creature tries to move in that direction the best it can. The parameters for this evolution is `numberOfGenerations = 20` and `populationSize = 10`. A demonstration of the various creatures generated as well as how they evolve can be seen [here](https://youtu.be/zjDQZgiCQqI) and a sample image below. Similar to the previous assignment, my algorithm creates horse like structures with legs on each side similar to the quadraped. A diagram below can be seen how to general structure of the horse is like. This was built using the community [r/ludobots](https://www.reddit.com/r/ludobots/) and depends on [Pyrosim](https://github.com/jbongard/pyrosim). 

## Running and Replaying
To run the following experiment use the following command:
```
python3 search.py
```
Note that running the entire experiment takes a bit of time depending on computer capabilities as there are 10 seeds and for each seed the following configuration (defined in `constansts.py`) totaling up to 10x500x10=**50,000 simulations**
```
numberOfGenerations = 500
populationSize = 10
```
Running `search.py` on my computer took approximately 2h 39m with the following laptop configuration
```
16 GB ram
Apple M1 Pro chip
```
Use the following command to replay specific evolved seeds
```
python3 replay.py 5 #input any seed number from 0-9
```
## Results
These were generated using `numpy.random.seed()`
![alt text](https://github.com/jeffersonxu/ludobots/blob/assignment8/fitness_curve.png)

## Diagram and Sample Image
![alt text](https://github.com/jeffersonxu/ludobots/blob/assignment8/diagram.jpg)
![alt text](https://github.com/jeffersonxu/ludobots/blob/assignment8/horse.png)

