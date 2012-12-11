# COPYRIGHT NOTICE: 
# This script Its Developed By DHDA STUDIO
# The purpose of this script its to develop a Component that
# Handle CSV Files, and manage it like a Index Data Base 
# # Copyright for the Script by Toussaint Jimenez, 2012. 
# The library is licensed under DHDA-IT-CODE Open Source License.

import os
import sys
import clr
import System
import StringIO
import math


# for accesssing GH classes
clr.AddReference("Grasshopper")
from Grasshopper.Kernel.Data import GH_Path
from Grasshopper import DataTree


#Variable Declaration and Casting Type
data = csvDataFields
index = (int(headerFieldIndex)) #Casting the Variable plus One to pass it in cmp sorted funtion


# Build a right list to be sorted by any Field
a = []
for i in data:
    splitData = i.split(',')
    for j in splitData:
        splitA = j.split(delimiter)
    a.append(splitA)


#dataTree = DataTree[object]()
#for i, thing in enumerate(data):
#    branch_id = branch_ids[i]
#    path = GH_Path(branch_id)
#    dataTree.Add(thing, path)
#a = dataTree



#Operation Sort by Index Field
xSortedList = sorted(a, cmp=lambda x, y: cmp(x[(index)], y[(index)]))

# Problem Here with the LIST IN LIST to a proper output to Grasshopper

#Operation Sorted List Transformation to GH DataTree to solve the list in list
wSortedList = DataTree[object]()                    #Call DataTree Internal GH List Object
for k in range(len(xSortedList)):                   #Star Loop the List in List Sorted
    branch_id = xSortedList[k]                      #Retrieve the (k)nth Item
    DataConverted = (delimiter).join(branch_id)     #Join the List to a Single String Line with the delimiter
    path = GH_Path(0)                               #Path Constructor
    wSortedList.Add(DataConverted, path)            #Append Operation to the List.

sortedList = wSortedList
#Enb Operation







