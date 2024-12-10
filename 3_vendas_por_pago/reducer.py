#!/usr/bin/python

import sys

salesTotal = 0
oldPayment = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisPayment, thisSale = data_mapped

    if oldPayment and oldPayment != thisPayment:
        oldPayment = thisPayment;
        salesTotal = 0

    oldPayment = thisPayment
    if float(salesTotal)<float(thisSale):
        salesTotal=thisSale

if oldPayment != None:
    print(oldPayment+"\t"+str(salesTotal))
