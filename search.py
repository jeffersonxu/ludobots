import matplotlib.pyplot as plt
from parallelHillClimber import PARALLEL_HILL_CLIMBER

phcs = []
for i in range(5):
    phc = PARALLEL_HILL_CLIMBER(i)
    phc.Evolve()
    phcs.append(phc)

for i, phc in enumerate(phcs):
    #phc.Show_Best()
    plt.plot(phc.fitness_history, label=f'Seed {i}')    

plt.ylabel("Average Fitness")
plt.xlabel("Generation")
plt.title("Average Fitness using Parallel Hill Climber for 5 Seeds")
plt.legend()
plt.show()
