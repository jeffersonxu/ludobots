import sys

from parallelHillClimber import PARALLEL_HILL_CLIMBER
from solution import SOLUTION
from simulation import SIMULATION

seedID = int(sys.argv[1])

directOrGUI = "GUI"
brainID = "best"
simulation = SIMULATION(directOrGUI, brainID, seedID, playBest=True)
simulation.RUN()
