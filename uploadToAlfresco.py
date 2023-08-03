import requests
import json

def uploadToAlfresco(path,fileName,alfURL,folderNodeID,child):
    nodeID = ''
    responseData = ''
    tempFileData = ''
    tempFile=''
    
    if fileName == '':
        fileName = "doctornote.jpg"

    #first step is to create the node

    _url = alfURL + "/alfresco/api/-default-/public/alfresco/versions/1/nodes/"+folderNodeID+"/children"

    if (child == ''):
        #dat = '{ "name": "'+ fileName +'","nodeType":"my:whitepaper"}'
        dat = '{ "name": "'+ fileName +'","nodeType":"my:cases"}'
    else:
        dat = '{ "name": "'+ fileName +'","nodeType":"rel:relatedCases"}'

        
    print("data for node create is:" + dat)
    jsonData = requests.post(_url, data = dat, auth = ('demo','demo'))

    #now need to get nodeID from response
    responseData = jsonData.json()
    print ("response is: " + str(responseData))

    nodeID = responseData["entry"]["id"]

    #now upload the node content
    #read the file into a buffer

    r = requests.put(alfURL+"/alfresco/api/-default-/public/alfresco/versions/1/nodes/"+nodeID+"/content",  auth=('demo','demo'), data=open(path + fileName, 'rb'))
    #print("result: "+r.text)


    return nodeID
