import requests

def updateNode(targetNodeID,caseID,plaintiff,defendent,alfURL,docID,DocFileName,DocType,DocFormat,Doctitle,Author,Recipient,Recipienttitle,RecipientAgency):
    _url = alfURL + "/alfresco/api/-default-/public/alfresco/versions/1/nodes/" + targetNodeID

    #data = "{\"properties\":{\"my:caseID\":\""+ caseID+ "\"}}"
    data = "{\"properties\":{\"my:caseID\":\""+ caseID+ "\",\"my:plaintiff\":\""+ plaintiff+ "\",\"my:defendant\":\""+ defendent+ "\"}}"  

    print("update data is: " + data)


    print (requests.put(_url,data,auth=('demo','demo')))
