# COPYRIGHT NOTICE: 
# This script Its Develped By DHDA STUDIO
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

from System.IO import StringReader
from LumenWorks.Framework.IO.Csv import CsvReader
# End of Importation

#Open the CSV file
file = open(filePath,"r")
data = file.read()

#Create component for reading CSV file 
csvReader = CsvReader(StringReader(data), True)
csvReader.SkipEmptyLines = True

#Get Indexes of source columns based on header.
headers = csvReader.GetFieldHeaders()
listHeaders = str(headers).split(separator)



#Get Data of source Based on File.
dataRead = CsvReader(StringReader(data), False)



csvlist = []                        #create a List to Store Csv Data
while dataRead.ReadNextRecord():    #Read each Record on the CSV file 
    row = []
    colCount = dataRead.FieldCount
    for i in range(colCount):       # Star Looping to Fill the row 
        row.append(dataRead[i])
    csvlist.append(row)

csvData = str(csvlist).split(",")   #return the list of Data to the Output

