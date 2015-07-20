#selectScript.py

import maya.cmds as cmds

window = cmds.window(title = 'Seleccinador de elementos', sizeable=False, resizeToFitChildren = False)
cmds.rowColumnLayout (numberOfColumns=2, columnWidth=[(1,100), (2,300)], columnOffset = [(1, 'right', 3)])

cmds.separator (h=10, style='none')
cmds.separator (h=10, style='none')   
 
cmds.text( label='Seleccinar objeto: ' )
objSelectField = cmds.textField('')

cmds.separator (h=10, style='none')
cmds.separator (h=10, style='none')  

cmds.separator (h=10, style='none')  

def buscar (objSelect, *pArgs):
    objSelect = cmds.textField (objSelectField, query=True, text=True)
    cmds.select(objSelect)


cmds.button (label='Buscar', command = buscar)

cmds.showWindow()
