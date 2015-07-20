#createRandomwithUI.py

import maya.cmds as cmds


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
    targetAtribbuteField = cmds.textField (text = 'rotateY')
    cmds.separator (h=10, style='none')
    
    #Tercera fila:
    cmds.separator (h=10, style='none')
    cmds.separator (h=10, style='none')
    cmds.separator (h=10, style='none')
    
    #Cuerta fila:
    cmds.separator (h=10, style='none')
    cmds.button (label='Apply', command=applyCallback)
    
    #Definimos la accion del bonton cancelar:
    def cancelCallback (*pArgs):
        if cmds.window (windowID, exists=True):
            cmds.deleteUI (windowID)
    cmds.button (label='Cancel', command=cancelCallback)
                
    cmds.showWindow()
    
#Definimos la accion del boton aplicar:
def applyCallback (*pArgs):
    print 'Apply button pressed.'
    
    
#Llamamos a la definciion para crear la ventana:
createUI ('My Title', applyCallback)
