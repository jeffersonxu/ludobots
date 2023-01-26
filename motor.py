import numpy
import pybullet as p
import constants as c
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
    
    def Prepare_To_Act(self):
        if self.jointName == b'Torso_BackLeg':            
            self.frequency = c.frequencyBack
            self.amplitude = c.amplitudeBack
            self.phaseOffset = c.phaseOffsetBack
        else:
            self.frequency = c.frequencyFront
            self.amplitude = c.amplitudeFront
            self.phaseOffset = c.phaseOffsetFront        
        
        self.motorValues = self.amplitude * numpy.sin(self.frequency * c.targetAngles + self.phaseOffset)

    def Set_Value(self, robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId, 
            jointName = self.jointName, 
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = 50)
