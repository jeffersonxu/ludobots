from world import WORLD
from robot import ROBOT
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time

class SIMULATION:    
    def __init__(self, directOrGUI):
        self.directOrGUI = directOrGUI
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)        
        self.world = WORLD()
        self.robot = ROBOT()

    def RUN(self):
        for i in range(1000):
            p.stepSimulation()    
            self.robot.SENSE(i)
            self.robot.Think()
            self.robot.ACT(i) 
            if self.directOrGUI == "GUI":
                time.sleep(1 / 1000)                        
    
    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()







