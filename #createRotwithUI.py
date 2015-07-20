#createRotwithUI.py

import maya.cmds as cmds
import functools


#Definimos la apariencia y contenido de la ventana:
def createUI (pWindowTitle, pApplyCallback):
    
    windowID = 'myWindowID'
    
    if cmds.window (windowID, exists=True):
        cmds.deleteUI (windowID)
        
    cmds.window (windowID, title = pWindowTitle, sizeable=False, resizeToFitChildren = False)
    
    cmds.rowColumnLayout (numberOfColumns=3, columnWidth=[(1,75), (2,60), (3,60)], columnOffset = [(1, 'right', 3)])
    
    #Primera fila:
    cmds.text (label = 'Prueba')
    startTimeField = cmds.intField (value = cmds.playbackOptions (q=True, minTime=True))
    endTimeField = cmds.intField (value = cmds.playbackOptions (q=True, maxTime=True))
    
    #Segunda fila:
    cmds.text (label = 'Prueba2')
    targetAttributeField = cmds.textField (text = 'rotateY')
    cmds.separator (h=10, style='none')
    
    #Tercera fila:
    cmds.separator (h=10, style='none')
    cmds.separator (h=10, style='none')
    cmds.separator (h=10, style='none')
    
    #Cuerta fila:
    cmds.separator (h=10, style='none')
    cmds.button (label='Apply', command= functools.partial(applyCallback, startTimeField, endTimeField,targetAttributeField))
    
    #Definimos la accion del bonton cancelar:
    def cancelCallback (*pArgs):
        if cmds.window (windowID, exists=True):
            cmds.deleteUI (windowID)
    cmds.button (label='Cancel', command=cancelCallback)
                
    cmds.showWindow()
    
#Definicion de la rotacion:
def keyFullRotation (pObjectName, pStartTime, pEndTime, pTargetAttribute):
    
     cmds.cutKey (pObjectName, time = (pStartTime, pEndTime), attribute=pTargetAttribute)
     cmds.setKeyframe (pObjectName, time = pStartTime, attribute=pTargetAttribute, value=0)
     cmds.setKeyframe (pObjectName, time = pEndTime, attribute=pTargetAttribute, value=360)
     cmds.selectKey (pObjectName, time = (pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True)
     cmds.keyTangent (inTangentType='linear', outTangentType='linear')
    
#Definimos la accion del boton aplicar:
def applyCallback (pApplyCallback, pStartTimeField, pEndTimeField,pTargetAttributeField, *pArgs):
      
    startTime = cmds.intField (pStartTimeField, query=True, value=True)
    endTime = cmds.intField (pEndTimeField, query=True, value=True)
    targetAtribbute = cmds.textField (pTargetAttributeField, query=True, text=True)
    
    selectionList = cmds.ls (selection=True, type='transform')
    
    for objectName in selectionList:
        keyFullRotation (objectName, startTime, endTime, targetAttribute)
    
#Llamamos a la definciion para crear la ventana:
createUI ('My Title', applyCallback)
