import requests

def updateNode(targetNodeID,alfURL,caseID,plaintiff,defendent,docID,DocFileName,DocType,DocFormat,Doctitle,Author,Recipient,Recipienttitle,RecipientAgency,foiaNotes):
    _url = alfURL + "/alfresco/api/-default-/public/alfresco/versions/1/nodes/" + targetNodeID

    #data = "{\"properties\":{\"my:caseID\":\""+ caseID+ "\"}}"    ,\"my:plaintiff\":\""+ plaintiff+ "\"
    data = "{\"properties\":{\"my:caseID\":\""+ caseID+ "\",\"my:plaintiff\":\""+ plaintiff+ "\",\"my:defendant\":\""+ defendent+ "\",\"my:DocID\":\""+ str(docID)+ "\",\"my:DocTitle\":\""+ Doctitle+ "\",\"my:Author\":\""+ Author+ "\",\"my:Recipient\":\""+ Recipient+ "\",\"my:RecipientTitle\":\""+ Recipienttitle+ "\",\"my:RecipientAgency\":\""+ RecipientAgency+ "\",\"my:DocType\":\""+ DocType+ "\",\"my:FOIANotes\":\""+ foiaNotes+ "\"}}"  

    print("update data is: " + data +" for nodeid: "+targetNodeID)

    print (requests.put(_url,data,auth=('demo','demo')))
