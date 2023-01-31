import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import numpy
import os
import constants as c

class ROBOT:
    
    def __init__(self, solutionID):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)        
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")
        os.system(f"rm brain{solutionID}.nndf")
        self.solutionID = solutionID

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    
    def SENSE(self, i):
        for linkName in self.sensors:
            self.sensors[linkName].Get_Value(i)

    def ACT(self, i):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)
    
    def Think(self):
        self.nn.Update()
        #self.nn.Print()
    
    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        f = open(f"tmp{self.solutionID}.txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.system(f"mv tmp{self.solutionID}.txt fitness{self.solutionID}.txt")
        