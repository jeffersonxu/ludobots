import copy
from solution import SOLUTION
from constants import numberOfGenerations

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()
    
    def Evolve(self):
        self.parent.Evaluate("DIRECT")
        for currentGeneration in range(numberOfGenerations):
            if not currentGeneration:
                self.Evolve_For_One_Generation("GUI")
            else:
                self.Evolve_For_One_Generation("DIRECT")
    
    def Evolve_For_One_Generation(self, directOrGUI):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(directOrGUI)
        self.Print()
        self.Select()
    
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child
    
    def Print(self):
        print(f"\n{self.parent.fitness} {self.child.fitness}\n")        

    def Show_Best(self):
        self.parent.Evaluate("GUI")