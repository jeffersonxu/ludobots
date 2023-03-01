import math
import random
import numpy

targetAngles = numpy.linspace(0, 2 * numpy.pi, 1000)

amplitudeBack = math.pi / 4
frequencyBack = 5
phaseOffsetBack = 0

amplitudeFront = math.pi / 4
frequencyFront = 10
phaseOffsetFront = math.pi / 4

numberOfGenerations = 20
populationSize = 10

numSensorNeurons = 9
numMotorNeurons = 8
motorJointRange = 0.2

