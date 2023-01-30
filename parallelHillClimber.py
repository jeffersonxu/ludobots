import copy
import os
from solution import SOLUTION
from constants import numberOfGenerations, populationSize

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1        
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
    
    def Evolve(self):        
        self.Evaluate(self.parents, "DIRECT")
        for currentGeneration in range(numberOfGenerations):            
            self.Evolve_For_One_Generation("DIRECT")                    
    
    def Evolve_For_One_Generation(self, directOrGUI):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children, directOrGUI)
        self.Print()
        self.Select()
    
    def Spawn(self):
        self.children = {}
        for key in self.parents.keys():
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for child in self.children.values():
            child.Mutate()

    def Select(self):
        for key in self.parents.keys():
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]        
    
    def Print(self):
        for key in self.parents.keys():            
            print(f"\n{self.parents[key].fitness} {self.children[key].fitness}\n")        

    def Show_Best(self):
        bestKey = min(self.parents.items(), key=lambda x: x[1].fitness)[0] 
        self.parents[bestKey].Start_Simulation("GUI")
    
    def Evaluate(self, solutions, directOrGUI):
        for parent in solutions.values():
            parent.Start_Simulation(directOrGUI)
        for parent in solutions.values():
            parent.Wait_For_Simulation_To_End()