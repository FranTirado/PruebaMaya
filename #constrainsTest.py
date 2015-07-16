#constrainsTest.py

import maya.cmds as cmds

#Crea una lista con el orden de seleccion
selectionList= cmds.ls(orderedSelection=True)

if len(selectionList) >= 2:
    print 'Select items: %s' %(selectionList)
    
    objectPrincipal = selectionList[0]
    
    selectionList.remove(objectPrincipal)
    
    #Crea una constrain para cada objeto seleccionado y le da una direccion
    for objectName in selectionList:
        cmds.aimConstraint(objectPrincipal, objectName, aimVector=[0,1,0])
    
else:
    print 'Please select two or more objests.'
