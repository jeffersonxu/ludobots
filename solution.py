import os
import time
import numpy
import pyrosim.pyrosim as pyrosim
import constants as c


class SOLUTION:
    def __init__(self, myID, links, joints, seed):
        self.links = links
        self.joints = joints
        self.sensor_num = sum([x['sensor_tag'] for x in links])
        self.weights = 2 * numpy.random.rand(self.sensor_num, len(joints)) - 1        
        self.myID = myID   
        self.seed = seed
        numpy.random.seed(seed)
    
    def Start_Simulation(self, directOrGui):
        self.Create_World()
        self.Generate_Brain()        
        os.system(f"python3 simulate.py {directOrGui} {self.myID} {self.seed} & 2&>1")

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
        randRow = numpy.random.randint(0, self.sensor_num)
        randCol = numpy.random.randint(0, len(self.joints))
        self.weights[randRow, randCol] = numpy.random.uniform(1, 3)
    
    def Set_ID(self, myID):
        self.myID = myID

