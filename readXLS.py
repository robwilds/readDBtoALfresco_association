#This is used to read from a native excel file (could use csv too)
#pip install pandas
import pandas as pd
import uploadToAlfresco
import makeChildAssociation as mca
import makeTargetAssociation as mta
import updateNode
from numpy import nan

#globals for 7.4 install
""" globalBaseURL = 'http://ec2-18-207-114-159.compute-1.amazonaws.com' #for 7.4 EC2
baseFolder = '29b8b116-75a1-4ee8-8909-25e1c0dfab87' #for 7.4 EC2 - Associations folder
hiddenFolder = '37d3c179-cf42-4f67-99ea-22bcabf763d7' """

#globals for 7.3 install
# globalBaseURL = 'http://ec2-3-90-226-222.compute-1.amazonaws.com' #for 7.3 EC2
# baseFolder = '2fdca4f6-f926-4819-b42e-b8fc993314e6' #for 7.4 EC2 - Associations folder
# hiddenFolder = 'e9ca1a5b-844a-4836-a55e-86eba511293c'

#globals for 7.4 DOJOLC install
globalBaseURL = 'http://ec2-3-83-206-117.compute-1.amazonaws.com'
baseFolder = 'c1bc5948-473c-453f-b81a-d2632ba46d58' #for 7.4 EC2 - Associations folder
hiddenFolder = '845a2bc5-0bdd-4b3a-8ec9-a494d83512b4'

fileName = '' #'doctornote.jpg'  #for testing
mainFile = ''
node2 = ''
node3 = ''
 
path = "Files for Search Tool/"
#path = "" #use this for testing


inputFile = path + "metadata.xlsx"
# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel(inputFile)
dataframe1.fillna(0, inplace=True)


for index, row in dataframe1.iterrows():
    
    if (row['DocID'] == ''): continue; #skip rows that don't have data
    print("**************************")
    print(str(row['DocID']),row['DocFileName'],row['UntzdPDF'],row['DocType'],row['DocFormat'],row['DocTitle'],row['Author'],row['Recipient'],row['RecipientTitle'],row['RecipientAgency'],row['FOIANotes'],row['POFilename'])
   
    #now process the main file and any associations
    mainFile = uploadToAlfresco.uploadToAlfresco(path,row['DocFileName'],globalBaseURL,baseFolder,'my:cases')

    updateNode.updateNode(mainFile,globalBaseURL,'','','',str(row['DocID']),row['DocFileName'],row['DocType'],row['DocFormat'],row['DocTitle'],row['Author'],str(row['Recipient']).replace("0",""),str(row['RecipientTitle']).replace("0",""),str(row['RecipientAgency']).replace("0",""),str(row['FOIANotes']).replace("0","")) #only update the target node

    if row['UntzdPDF'] != 0:
        child1 = uploadToAlfresco.uploadToAlfresco(path,row['UntzdPDF'],globalBaseURL,baseFolder,'rel:relatedCases') #change folder to hidden
        #this associates the child with the parent
        print (mta.makeTargetAssociation(child1,mainFile,globalBaseURL,"my:relatedCaseInfo"))
        #this associates the parent with the child
        print (mta.makeTargetAssociation(mainFile,child1,globalBaseURL,"rel:parentCase"))


    if row['POFilename'] != 0:
        child2 = uploadToAlfresco.uploadToAlfresco(path,row['POFilename'],globalBaseURL,baseFolder,'rel:relatedCases') #change folder to hidden
         #this associates the child with the parent
        print (mta.makeTargetAssociation(child2,mainFile,globalBaseURL,"my:relatedCaseInfo"))
        #this associates the parent with the child
        print (mta.makeTargetAssociation(mainFile,child2,globalBaseURL,"rel:parentCase"))




