# COPYRIGHT NOTICE: 
# This script Its Developed By DHDA STUDIO
# The purpose of this script its to develop a Component that
# Handle CSV Files, and manage it like a Index Data Base 
# # Copyright for the Script by Toussaint Jimenez, 2012. 
# The library is licensed under DHDA-IT-CODE Open Source License.

# COPYRIGHT NOTICE: 
# This script uses the CSV reader by Sebastien Lorion 
# You can find his library including source code  
# at http://www.codeproject.com/cs/database/CsvReader.asp. 
# Copyright for the CSV library by Sbastien Lorion, 2005. 
# The library is licensed under MIT Open Source License. 


# Necessary imports to enable access to CSV reading component
import os
import sys
import clr
import System


from System import *

# for accesssing GH classes
clr.AddReference("Grasshopper")
from Grasshopper.Kernel.Data import GH_Path
from Grasshopper import DataTree

# Importation of the CSV Reader .Net Library By Sebastien Lorion
from System.Reflection import Assembly
assemblyPath = "C:\Program Files\Rhinoceros 5.0 Evaluation (64-bit)\Plug-ins\IronPython\Lib\csv_reader\LumenWorks.Framework.IO.dll"  #path of the CSV Reader By Sebastien Lorion, Change to yours path
assembly = Assembly.LoadFile(assemblyPath)
clr.AddReference(assembly)

from System.IO import StreamReader
from LumenWorks.Framework.IO.Csv import CsvReader
# End of Importation

#Create Operation for Open and reading CSV file 
csvFile = CsvReader(StreamReader(filePath), True) 
csvFile.SkipEmptyLines = True
#End of the Operation


#Create Operation Header
header = [csvFile.GetFieldHeaders()]                 # Retrieve the Csv Header
csvHeader = header[0]                                # Call the Header
headerstr = csvHeader[0]                             # release the Header from the internal Array
headerFields = headerstr.split(delimiter)       # List of the Fields in GH Data type
#End of the Operation

#Raw Csv Data
csvRawData = csvFile.GetCurrentRawData()
#End of the Operation

#Operation Data Csv File 
contentData = []
while csvFile.ReadNextRecord():
    contentCount = csvFile.FieldCount
    for i in range (contentCount):                       #Start Looping to Fill ContentData with CSV File RawData
        contentData.append(csvFile[i])


csvDataFields = contentData[rowStart:rowEnd]



#Operation for Graft The Data
newlist = []
newlist = csvDataFields[:]

graftedTree = DataTree[object]()
for i in range(len(newlist)):
    str =newlist[i]
    path = GH_Path(i)
    graftedTree.AddRange([str],path)

graftedData = graftedTree
#End of the Graft

