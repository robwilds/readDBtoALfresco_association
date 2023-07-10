import mysql.connector
import uploadToAlfresco
import makeTargetAssociation
import makeChildAssociation as mca
import updateNode

#globals for 7.4 install
globalBaseURL = 'http://ec2-18-207-114-159.compute-1.amazonaws.com' #for 7.4 EC2
baseFolder = '29b8b116-75a1-4ee8-8909-25e1c0dfab87' #for 7.4 EC2 - Associations folder
hiddenFolder = '37d3c179-cf42-4f67-99ea-22bcabf763d7'

#globals for 7.3 install
""" globalBaseURL = 'http://ec2-3-90-226-222.compute-1.amazonaws.com' #for 7.3 EC2
baseFolder = '22515311-84c6-48ba-971f-8ea08cd56628' #for 7.4 EC2 - Associations folder
hiddenFolder = '37d3c179-cf42-4f67-99ea-22bcabf763d7' """

fileName = 'doctornote.jpg'  #for testing
targetNode = ''
node2 = ''
node3 = ''
""" 
#PROTOTYPING BELOW
targetNode = uploadToAlfresco.uploadToAlfresco('doctornote.jpg',globalBaseURL,baseFolder)
print (targetNode+"\n")

#upload another file
node2 = uploadToAlfresco.uploadToAlfresco('meeting.jpg',globalBaseURL,baseFolder) #change folder to hidden
print (node2)

#upload yet another file
node3 = uploadToAlfresco.uploadToAlfresco('fatherson.jpg',globalBaseURL,baseFolder) #change folder to hidden
print (node3)

#now make the assocation..this is one way..from the main doc to the associated..if you want 
#to make association the other way, then re run the function and switch the nodeids
print (makeTargetAssociation.makeTargetAssociation(node2,targetNode,globalBaseURL))
print (makeTargetAssociation.makeTargetAssociation(node3,targetNode,globalBaseURL))
#### END PROTOTYPING
 """


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='sys',
                                         user='root',
                                         password='wart9667')

    sql_select_Query = "select * from cases"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0])
        print("caseID = ", row[1])
        print("plaintiff  = ", row[2])
        print("defendant =", row[3])
        print("mainfile  = ", row[4])
        print("assoc1 =", row[5])
        print("assoc2 =", row[6])

        targetNode = uploadToAlfresco.uploadToAlfresco(row[4],globalBaseURL,baseFolder)
        updateNode.updateNode(targetNode,row[1],row[2],row[3],globalBaseURL) #only update the target node
        
        if row[5] != '':
            node2 = uploadToAlfresco.uploadToAlfresco(row[5],globalBaseURL,baseFolder) #change folder to hidden
            #print (makeTargetAssociation.makeTargetAssociation(node2,targetNode,globalBaseURL))
            print (mca.makeChildAssociation(node2,targetNode,globalBaseURL))

        if row[6] != '':
            node3 = uploadToAlfresco.uploadToAlfresco(row[6],globalBaseURL,baseFolder) #change folder to hidden
            #print (makeTargetAssociation.makeTargetAssociation(node3,targetNode,globalBaseURL))
            print (mca.makeChildAssociation(node3,targetNode,globalBaseURL))


except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")