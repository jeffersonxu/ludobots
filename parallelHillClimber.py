import copy
import os
import matplotlib.pyplot as plt
import pyrosim.pyrosim as pyrosim
from solution import SOLUTION
from constants import numberOfGenerations, populationSize
from horse import Generate_Horse

class PARALLEL_HILL_CLIMBER:
    def __init__(self, seed):
        self.parents = {}
        self.nextAvailableID = 0
        self.seed = seed
        
        links, joints = Generate_Horse(seed)
        pyrosim.Start_URDF("body.urdf")
        for link_dict in links:
            pyrosim.Send_Cube(name=link_dict['name'], pos=link_dict['pos'], size=link_dict['size'], color=link_dict['color'], color_name=link_dict['color_name'])
        for joint_dict in joints:
            pyrosim.Send_Joint(name=joint_dict['name'], parent=joint_dict['parent'], child=joint_dict['child'], type = "revolute", position=joint_dict['position'], jointAxis=joint_dict['jointAxis'])
        pyrosim.End()

        for i in range(populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID, links, joints, seed)
            self.nextAvailableID += 1        

        self.fitness_history = []
        
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
        #self.Print()
        self.Select()
        self.Save()
    
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
        sorted_parents = sorted(self.parents.items(), key=lambda x: x[1].fitness)
        self.parents[bestKey].Start_Simulation("GUI")

        print(f"best parent {sorted_parents[-1][1].myID} of seed-{self.seed}:",sorted_parents[-1][1].fitness)
        os.system(f"cp body.urdf data/seed{self.seed}")
        os.system(f"cp -n brain*.nndf data/seed{self.seed}/brain_best.nndf")
    
    def Evaluate(self, solutions, directOrGUI):
        for parent in solutions.values():
            parent.Start_Simulation(directOrGUI)
        for parent in solutions.values():
            parent.Wait_For_Simulation_To_End()
    
    def Save(self):
        bestKey = min(self.parents.items(), key=lambda x: x[1].fitness)[0]
        self.fitness_history.append(self.parents[bestKey].fitness)
            