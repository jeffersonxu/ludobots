import os
import time
import numpy
import random
import pyrosim.pyrosim as pyrosim
import constants as c

class SOLUTION:
    def __init__(self, myID):
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1
        self.myID = myID
    
    def Start_Simulation(self, directOrGui):
        self.Create_World()
        self.Generate_Body()
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
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[1,1,1])
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])

        pyrosim.Send_Joint(name = "FrontLeg_FrontLeg2" , parent= "FrontLeg" , child = "FrontLeg2" , type = "revolute", position = [0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg2", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0, -0.5, 1], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2])

        pyrosim.Send_Joint(name = "BackLeg_BackLeg2" , parent= "BackLeg" , child = "BackLeg2" , type = "revolute", position = [0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg2", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint(name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5, 0, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0] , size=[1,0.2,0.2])

        pyrosim.Send_Joint(name = "LeftLeg_LeftLeg2" , parent= "LeftLeg" , child = "LeftLeg2" , type = "revolute", position = [-1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg2", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint(name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5, 0, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0] , size=[1,0.2,0.2])

        pyrosim.Send_Joint(name = "RightLeg_RightLeg2" , parent= "RightLeg" , child = "RightLeg2" , type = "revolute", position = [1, 0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg2", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        pyrosim.Send_Sensor_Neuron(name=0 , linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1 , linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2 , linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="FrontLeg2")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="BackLeg2")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="LeftLeg2")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="RightLeg2")

        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=13, jointName="FrontLeg_FrontLeg2")
        pyrosim.Send_Motor_Neuron(name=14, jointName="BackLeg_BackLeg2")
        pyrosim.Send_Motor_Neuron(name=15, jointName="LeftLeg_LeftLeg2")
        pyrosim.Send_Motor_Neuron(name=16, jointName="RightLeg_RightLeg2")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        randRow = random.randint(0, c.numSensorNeurons - 1)
        randCol = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randRow][randCol] = random.random() * 2 + 1
    
    def Set_ID(self, myID):
        self.myID = myID