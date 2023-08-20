import requests

def makeTargetAssociation(targetNodeID,currentNodeID,alfURL,modelName):
    _url = alfURL + "/alfresco/api/-default-/public/alfresco/versions/1/nodes/" + currentNodeID + "/targets"

    data = '{"targetId": "' + targetNodeID + '","assocType": "' +modelName + '"}'
    
    return requests.post(_url,data,auth=('demo','demo'))
