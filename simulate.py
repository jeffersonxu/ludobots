import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import numpy
import time
import math

amplitudeBack = math.pi
frequencyBack = 5
phaseOffsetBack = math.pi / 2

targetAnglesBackX = numpy.linspace(0, 2 * numpy.pi, 1000)
targetAnglesBack = amplitudeBack * numpy.sin(frequencyBack * targetAnglesBackX + phaseOffsetBack) / 4
numpy.save("data/angleValuesBack", targetAnglesBack)

amplitudeFront = math.pi * 1.5
frequencyFront = 10
phaseOffsetFront = 0

targetAnglesFrontX = numpy.linspace(0, 2 * numpy.pi, 1000)
targetAnglesFront = amplitudeFront * numpy.sin(frequencyFront * targetAnglesFrontX + phaseOffsetFront) / 4
numpy.save("data/angleValuesFront", targetAnglesFront)

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robotId)
p.loadSDF("world.sdf")
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

for i in range(1000):
    time.sleep(1 / 1200)    
    p.stepSimulation()    
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")   
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")     
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId, 
        jointName = b'Torso_BackLeg', 
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAnglesBack[i],
        maxForce = 100)

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg', 
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAnglesFront[i],
        maxForce = 100)

    print(i)

numpy.save("data/backLegSensorValues", backLegSensorValues)
numpy.save("data/frontLegSensorValues", frontLegSensorValues)

p.disconnect()