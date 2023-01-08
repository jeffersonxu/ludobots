import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

pyrosim.Start_SDF("box.sdf")
for i in range(10):
    pyrosim.Send_Cube(name="Box", pos=[x, y, z + i * 1] , size=[width,length,height])
    length *= 0.9
    width *= 0.9
    height *= 0.9
    z *= 0.9
pyrosim.End()
