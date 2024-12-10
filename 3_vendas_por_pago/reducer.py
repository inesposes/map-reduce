#!/usr/bin/python

import sys

salesTotal = 0
oldCategory = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisCategory, thisSale = data_mapped

    if oldCategory and oldCategory != thisCategory:
        oldCategory = thisCategory;
        salesTotal = 0

    oldCategory = thisCategory
    if float(salesTotal)<float(thisSale):
        salesTotal=thisSale

if oldCategory != None:
    print(oldCategory+"\t"+str(salesTotal))
