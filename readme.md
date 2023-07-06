# This project will read from a sql database and put files and meta-data in to alfresco.  the "related" docs are set as associations on the primary document

## Pre-requisites

make sure python3 mysql connector are installed. 

the files that will be fectched will be stored locally to the python script

when the first file column is read, that is sent to alfresco...the resulting nodeid is used as the target for the remaining two files that are associated to the first file

FLOW

read column a
Get file and upload to Alfresco
store nodeIDa
Ready column b
Get file and upload to Alfresco
store nodeIDb
create association between nodeIDa and nodeIDb
Ready column c
Get file and upload to Alfresco
store nodeIDc
create association between nodeIDa and nodeIDc

