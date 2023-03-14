# ludobots
This contains the final project for Northwestern CS 396: Artifical Life. In short, this project uses the parallel hill climber to design morphology and behavior for locomotion with a fitness algorithm of the general negative X direction. My algorithm creates horse like structures with legs on each side similar to the quadraped. This was built using the community [r/ludobots](https://www.reddit.com/r/ludobots/) and depends on [Pyrosim](https://github.com/jbongard/pyrosim). 

## Methods
Methods. Explain what you did and how you did it. Where is the code to do each step? How do you run it? Cartoons of the genotype-to-phenotype map (how brains/bodies are encoded and expressed to form a robot), mutations (explain all the ways to make offspring and how they can be dis/similar to parents), selection (how does the parallel hill climber or whatever algo you use, work?)

The experiment starts off in `search.py` which utilizes the `PARALLEL_HILL_CLIMBER` class. Within this class we can see the main structure used for  evolution in `parallellHillClimber.py`
```python
def Evolve_For_One_Generation(self, directOrGUI):
    self.Spawn()
    self.Mutate()
    self.Evaluate(self.children, directOrGUI)
    #self.Print()
    self.Select()
    self.Save()
```

### What is Paralell Hill Climbing?
Imagine you are trying to climb a hill and you can only move up or down. You start at the bottom of the hill and keep trying different paths until you find the highest point. Now imagine there are several people trying to climb the same hill at the same time. Each person takes a different path, and they all try to find the highest point. Once everyone reaches the top, they compare their heights and choose the person who climbed the highest as the winner. Parallel Hill Climbing is similar to this idea. Instead of people, we use computer programs to try different solutions to a problem. Each program takes a different approach and tries to find the best solution. Once all the programs have finished, we compare their results and choose the program that found the best solution as the winner. This method is often used to solve optimization problems, where we want to find the best solution out of many possible solutions.






![alt text](https://github.com/jeffersonxu/ludobots/blob/assignment8/diagram.jpg)
![alt text](https://github.com/jeffersonxu/ludobots/blob/assignment8/horse.png)

### Running and Replaying
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
After each seed finishing running an entire experiment of 10 parents each with 500 generations, fitness of the best creature in the population at each generation was recorded. The figure below shows all 10 seeds over each generation graphed. The more negative the fitness was, the better that generation performed as the goal was to move in the negative X direction. It was clear that evolution occurred seeing the fitness curves for each seed gradually become more negative. Seed 2 seemed to have performed the best and most seeds after 300 generations seemed to have flattened off in their fitness. For the future, perhaps more diverse mutations could help evolve creatures as I only had time to implement a very simple mutation algorithm, limiting beneficial mutations. Additionally, my horse creature was still simple and could have more complex features that can be added such as a more complex torso. It was clear that through the paralell hill climber that seeds were able to evolve generations of creature that were ultimately able to move somewhat well.
![alt text](https://github.com/jeffersonxu/ludobots/blob/assignment8/diagramFINAL.png)


