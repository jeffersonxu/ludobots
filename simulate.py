import sys
from simulation import SIMULATION

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
seedID = sys.argv[3]

simulation = SIMULATION(directOrGUI, solutionID, seedID)
simulation.RUN()
simulation.Get_Fitness()