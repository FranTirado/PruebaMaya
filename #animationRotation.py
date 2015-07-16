#animationRotation.py

import maya.cmds as cmds

selectionList = cmds.ls(selection=True, type='transform')

if len(selectionList)>=1:
    print 'Select items: %s' %(selectionList)
    
    startTime = cmds.playbackOptions (query=True, minTime=True)
    endTime = cmds.playbackOptions (query=True, maxTime=True)
    
    for objectName in selectionList:
        
        objectTypeResult = cmds.objectType (objectName)
        
        cmds.cutKey (objectName, time = (startTime, endTime), attribute='rotateY')
        cmds.setKeyframe (objectName, time = startTime, attribute='rotateY', value=0)
        cmds.setKeyframe (objectName, time = endTime, attribute='rotateY', value=360)
        cmds.selectKey (objectName, time = (startTime, endTime), attribute='rotateY', keyframe=True)
        cmds.keyTangent (inTangentType='linear', outTangentType='linear')
        
else:
    print 'Please select two or more objests.'
