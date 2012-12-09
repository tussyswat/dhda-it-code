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
index = (int(headerFieldIndex)+1) #Casting the Variable plus One to pass it in cmp sorted funtion

# Build a right list to be sorted by any Field
a = []
for i in data:
    splitData = i.split(',')
    for j in splitData:
        splitA = j.split(delimiter)
    a.append(splitA)

# Operation Sort by Index Field
xSortedList = sorted(a, cmp=lambda x, y: cmp(x[(index)], y[(index)]))

# Problem Here with the LIST IN LIST to a proper output to Grasshopper
sortedList = xSortedList













"""
fxSortedList = reduce(lambda x, y: x+y, xSortedList) #Flatterned List

n1 = len(data) # Length of data list
n2 = len(fxSortedList) #Length of Flatterned and Sorted List 
n = int(n2/n1)

sortedList = [fxSortedList[i:i+n] for i in range(0, n2, n)]

print sortedList
"""



