import requests

def makeChildAssociation(targetNodeID,currentNodeID,alfURL,modelName):
    _url = alfURL + "/alfresco/api/-default-/public/alfresco/versions/1/nodes/" + currentNodeID + "/secondary-children" #used for children association
    
    data = '{"childId": "' + targetNodeID + '","assocType": "' +modelName+ '"}'
    return requests.post(_url,data,auth=('demo','demo'))
