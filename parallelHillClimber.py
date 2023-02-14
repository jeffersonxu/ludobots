import copy
import os
import random
import pyrosim.pyrosim as pyrosim
from solution import SOLUTION
from constants import numberOfGenerations, populationSize

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        
        num_links = random.randint(4, 10)
        links = Generate_Snake_Links(num_links)
        joints = Generate_Snake_Joints(links, num_links)

        pyrosim.Start_URDF("body.urdf")
        for i in range(num_links):
            pyrosim.Send_Cube(name=links[i]['name'], pos=links[i]['pos'], size=links[i]['size'], color=links[i]['color'], color_name=links[i]['color_name'])
            if i < num_links - 1:
                pyrosim.Send_Joint(name=joints[i]['name'], parent=joints[i]['parent'], child=joints[i]['child'], type = "revolute", position=joints[i]['position'], jointAxis=joints[i]['jointAxis'])
        pyrosim.End()

        for i in range(populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID, links, joints)
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
            

def Generate_Snake_Links(num_links):
    links = []
    for i in range(num_links):
        size_range = (0.2, 1)
        size_x = random.uniform(size_range[0], size_range[1])
        size_y = random.uniform(size_range[0], size_range[1])
        size_z = random.uniform(size_range[0], size_range[1])
        
        if i:
            pos_x = size_x / 1.5
            pos_y = 0
            pos_z = size_z / 1.5 - links[i - 1]['size'][2] / 1.5        
        else:        
            pos_x = size_x / 1.5
            pos_y = 0
            pos_z = size_z / 1.5


        if random.random() > 0.5:
            color_name = 'green'
            link_color = '0 1.0 0 1.0'
            sensor_tag = True
        else:
            color_name = 'blue'
            link_color = '0 0 1.0 1.0'
            sensor_tag = False

        link_dict = {
            "name": f"link{i}",
            "pos": [pos_x, pos_y, pos_z],
            "size": [size_x, size_y, size_z],
            'sensor_tag': sensor_tag,
            'color': link_color,
            'color_name': color_name
        }
        links.append(link_dict)
    
    return links

def Generate_Snake_Joints(links, num_links):
    joints = []
    for i in range(num_links - 1):
        parent = links[i]['name'] 
        child = links[i + 1]['name']        
        parent_size = links[i]['size'][2]
        if i:
            parent_parent_size_z = links[i - 1]['size'][2]
            position_x = links[i]['size'][0]
            position_y = 0
            position_z = parent_size / 1.5 - parent_parent_size_z / 1.5
        else:
            position_x = links[i]['size'][0]
            position_y = 0
            position_z = parent_size / 1.5 

        joint_dict = {
            'name': f'{parent}_{child}',
            'parent': parent,
            'child': child, 
            'position': [position_x, position_y, position_z],
            'jointAxis': '0 0 1' if random.random() > 0.5 else '0 1 0'
        }
        joints.append(joint_dict)

    return joints