import os
import time
import numpy
import random
import pyrosim.pyrosim as pyrosim
import constants as c

class SOLUTION:
    def __init__(self, myID, links, joints):
        self.links = links
        self.joints = joints
        self.sensor_num = sum([x['sensor_tag'] for x in links])
        self.weights = 2 * numpy.random.rand(self.sensor_num, len(joints)) - 1        
        self.myID = myID   
    
    def Start_Simulation(self, directOrGui):
        self.Create_World()
        #self.Generate_Body()
        self.Generate_Brain()        
        os.system(f"python3 simulate.py {directOrGui} {self.myID} & 2&>1")

    def Wait_For_Simulation_To_End(self):        
        fitnessFileName = f"fitness{self.myID}.txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        fitnessFile = open(fitnessFileName, "r")
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()
        os.system(f"rm {fitnessFileName}")

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")      
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")  
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.25] , size=[1, 3, 0.5])

        pyrosim.Send_Joint(name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5, 0.5, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[.5, 0.25, 0] , size=[2, 0.2, 0.5])
        pyrosim.Send_Joint(name = "RightLeg_RightLeg2" , parent= "RightLeg" , child = "RightLeg2" , type = "revolute", position = [1.5, 0.25, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg2", pos=[0, 0, -.5] , size=[0.2, 0.2, 1.5])

        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0.5, -0.5, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, -0.25, 0] , size=[2, .2, 0.5])
        pyrosim.Send_Joint(name = "FrontLeg_FrontLeg2" , parent= "FrontLeg" , child = "FrontLeg2" , type = "revolute", position = [1.5, -.25, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontLeg2", pos=[0, 0, -.5] , size=[.2, 0.2, 1.5])

        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-0.5, -0.5, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[-.5, -0.25, 0] , size=[2, 0.2, 0.5])
        pyrosim.Send_Joint(name = "BackLeg_BackLeg2" , parent= "BackLeg" , child = "BackLeg2" , type = "revolute", position = [-1.5, -0.25, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BackLeg2", pos=[0, 0, -.5] , size=[0.2, 0.2, 1.5])

        pyrosim.Send_Joint(name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5, 0.5, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-.5, 0.25, 0] , size=[2, 0.2, 0.5])
        pyrosim.Send_Joint(name = "LeftLeg_LeftLeg2" , parent= "LeftLeg" , child = "LeftLeg2" , type = "revolute", position = [-1.5,0.25,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg2", pos=[0, 0, -.5] , size=[0.2, 0.2, 1.5])

        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        curr_id = 0
        for i in range(len(self.links)):
            if self.links[i]['sensor_tag']:
                pyrosim.Send_Sensor_Neuron(name = curr_id , linkName = self.links[i]['name'])
                curr_id += 1

        for i in range(len(self.joints)):
            pyrosim.Send_Motor_Neuron(name = curr_id , jointName = self.joints[i]['name'])
            curr_id += 1

        for currentRow in range(self.sensor_num):
            for currentColumn in range(len(self.joints)):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + self.sensor_num , weight = self.weights[currentRow][currentColumn] )
        pyrosim.End()

    def Mutate(self):
        randRow = random.randint(0, self.sensor_num - 1)
        randCol = random.randint(0, len(self.joints) - 1)
        self.weights[randRow][randCol] = random.random() * 2 + 1
    
    def Set_ID(self, myID):
        self.myID = myID

