import requests

def makeChildAssociation(targetNodeID,currentNodeID,alfURL):
    _url = alfURL + "/alfresco/api/-default-/public/alfresco/versions/1/nodes/" + currentNodeID + "/secondary-children"

    data = '{"childId": "' + targetNodeID + '","assocType": "my:relatedCaseInfo"}'
    return requests.post(_url,data,auth=('demo','demo'))
