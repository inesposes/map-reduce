#!/usr/bin/python

import sys

maxSale = 0
maxPayment = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    _, thisValue = data_mapped
    cost, payment =thisValue.strip().split(",")

    if maxSale<float(cost):
        maxPayment=payment
        maxSale=float(cost)

if maxPayment != None:
    print(maxPayment+"\t"+str(maxSale))
