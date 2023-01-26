from world import WORLD
from robot import ROBOT
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time

class SIMULATION:    
    def __init__(self):
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
            time.sleep(1 / 1000)
            #print(i)

    def __del__(self):
        p.disconnect()







