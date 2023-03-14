# ludobots
This contains assignment 8 for Northwestern CS 396: Artifical Life. Specifically, this assignment uses the parallel hill climber to design morphology and behavior for locomotion. The fitness algorithm is the general negative X direction so each creature tries to move in that direction the best it can. The parameters for this evolution is `numberOfGenerations = 20` and `populationSize = 10`. A demonstration of the various creatures generated as well as how they evolve can be seen [here](https://youtu.be/zjDQZgiCQqI) and a sample image below. Similar to the previous assignment, my algorithm creates horse like structures with legs on each side similar to the quadraped. A diagram below can be seen how to general structure of the horse is like. This was built using the community [r/ludobots](https://www.reddit.com/r/ludobots/) and depends on [Pyrosim](https://github.com/jbongard/pyrosim). 

## Methods
![alt text](https://github.com/jeffersonxu/ludobots/blob/assignment8/diagram.jpg)
![alt text](https://github.com/jeffersonxu/ludobots/blob/assignment8/horse.png)

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
To adjust the number of seeds go to `search.py` and change the following
```python
for i in range(10): #change 10 to whichever number of seeds you desire
    phc = PARALLEL_HILL_CLIMBER(i)
    phc.Evolve()
    phcs.append(phc)
    phc.Show_Best()
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
After each seed finishing running an entire experiment of 10 parents each with 500 generations, fitness of the best creature in the population at each generation was recorded. The figure below shows all 10 seeds over each generation graphed. The more negative the fitness was, the better that generation performed as the goal was to move in the negative X direction. Seed 2 seemed to have performed the best and most seeds after 300 generations seemed to have flattened off in their fitness. For the future, perhaps more diverse mutations could help evolve creatures as I only had time to implement a very simple mutation algorithm. Additionally, my horse creature was still simple and could have more complex features that can be added such as a more complex torso. It was clear that through the paralell hill climber that seeds were able to evolve generations of creature that were ultimately able to move somewhat well.
![alt text](https://github.com/jeffersonxu/ludobots/blob/assignment8/diagramFINAL.png)

