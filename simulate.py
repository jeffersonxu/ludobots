import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import numpy
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robotId)
p.loadSDF("world.sdf")
backLegSensorValues = numpy.zeros(500)
frontLegSensorValues = numpy.zeros(500)

for i in range(500):
    time.sleep(1 / 60)    
    p.stepSimulation()    
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")   
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")               
    print(i)

numpy.save("data/backLegSensorValues", backLegSensorValues)
numpy.save("data/frontLegSensorValues", frontLegSensorValues)

p.disconnect()