#This is used to read from a native excel file (could use csv too)
#pip install pandas
import pandas as pd
import uploadToAlfresco
import makeChildAssociation as mca
import updateNode
from numpy import nan

#globals for 7.4 install
""" globalBaseURL = 'http://ec2-18-207-114-159.compute-1.amazonaws.com' #for 7.4 EC2
baseFolder = '29b8b116-75a1-4ee8-8909-25e1c0dfab87' #for 7.4 EC2 - Associations folder
hiddenFolder = '37d3c179-cf42-4f67-99ea-22bcabf763d7' """

#globals for 7.3 install
globalBaseURL = 'http://ec2-3-90-226-222.compute-1.amazonaws.com' #for 7.3 EC2
baseFolder = '2fdca4f6-f926-4819-b42e-b8fc993314e6' #for 7.4 EC2 - Associations folder
hiddenFolder = 'e9ca1a5b-844a-4836-a55e-86eba511293c'

fileName = '' #'doctornote.jpg'  #for testing
targetNode = ''
node2 = ''
node3 = ''
 
# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('metadata.xlsx')
dataframe1.fillna(0, inplace=True)


for index, row in dataframe1.iterrows():
    
    if (row['DocID'] == ''): continue; #skip rows that don't have data
    print(str(row['DocID']),row['DocFileName'],row['UntzdPDF'],row['DocType'],row['DocFormat'],row['DocTitle'],row['Author'],row['Recipient'],row['RecipientTitle'],row['RecipientAgency'],row['FOIANotes'],row['POFilename'])
   
    #now process the main file and any associations
    targetNode = uploadToAlfresco.uploadToAlfresco(row['DocFileName'],globalBaseURL,baseFolder,'')

    updateNode.updateNode(targetNode,globalBaseURL,'','','',str(row['DocID']),row['DocFileName'],row['DocType'],row['DocFormat'],row['DocTitle'],row['Author'],row['Recipient'],row['RecipientTitle'],row['RecipientAgency'],str(row['FOIANotes'])) #only update the target node

    if row['UntzdPDF'] != 0:
            node2 = uploadToAlfresco.uploadToAlfresco(row['UntzdPDF'],globalBaseURL,baseFolder,'child') #change folder to hidden
            #print (makeTargetAssociation.makeTargetAssociation(node2,targetNode,globalBaseURL))
            print (mca.makeChildAssociation(node2,targetNode,globalBaseURL))

    if row['POFilename'] != 0:
            node3 = uploadToAlfresco.uploadToAlfresco(row['POFilename'],globalBaseURL,baseFolder,'child') #change folder to hidden
            #print (makeTargetAssociation.makeTargetAssociation(node3,targetNode,globalBaseURL))
            print (mca.makeChildAssociation(node3,targetNode,globalBaseURL))



