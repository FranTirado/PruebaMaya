#createRandom.py

import maya.cmds as cmds
import random

random.seed(1234)


'''
#Crea una lista con los cubos creados
cubeList = cmds.ls('myCube*')
if len(cubeList)>0:
    cmds.delete(cubeList)
#Crea un cubo de 1x1x1 y lo nombra
result = cmds.polyCube (w=1, h=1, d=1, name='miCubo#')
'''

#Crea conforme al orden del selección el en viewport
result = cmds.ls(orderedSelection=True)

print 'result: %s' %(result)

transformName = result[0]

#Crea un grupo para los cubos creados
instanceGroupName = cmds.group( empty=True, name=transformName + '_instance_grp#')

#Crea cubos como instancias de forma random
for i in range(0, 20):
    instanceResult = cmds.instance(transformName, name=transformName + '_instance#')
    
    cmds.parent(instanceResult, instanceGroupName)
    
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)
    z = random.uniform(-10, 10)
    
    cmds.move(x,y,z, instanceResult)
    
    xRot = random.uniform(0, 360)
    yRot = random.uniform(0, 360)
    zRot = random.uniform(0, 360)
    
    cmds.rotate( xRot, yRot, zRot, instanceResult)
    
    scalingFactor = random.uniform(0.3, 1.5)
    
    cmds.scale(scalingFactor, scalingFactor, scalingFactor, instanceResult)
    
cmds.hide( transformName)
cmds.xform (instanceGroupName, centerPivots=True)
