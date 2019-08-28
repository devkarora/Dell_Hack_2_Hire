import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from random import randrange, uniform

def calculateCostOfLaptop(gc, hdd, keyboard, mouse, processor, ram, screen):
	choosenprocessor = processor

	choosenram = 'RAM '+ram

	choosenkeyboard = 'KEYBOARD '+keyboard

	choosenscreen = 'screen '+screen

	if mouse == 'Traditional':
		choosenmouse = 'MOUSE 3 Click'
	else:
		choosenmouse = 'MOUSE 5 Click'

	choosenhdd = 'HDD '+hdd

	choosengc = 'Graphic card '+gc

	commodity = []
	component = []
	supplier = []
	cost = []
	supplierP = []
	componentP = []
	#with open('faban.txt') as fobj:
	#    for line in fobj:
	#        row = line.split()
	#        data.append(row[:-1])
	#        target.append(row[-1])

	with open('dataset.csv') as csvfile:
	    readCSV = csv.reader(csvfile, delimiter=',')
	    for row in readCSV:
	        commodity.append(row[0])
	        component.append(row[1])
	        supplier.append(row[2])
	        cost.append(row[3])
	        supplierP.append(row[4])
	        componentP.append(row[5])

	commodityP = []
	commodityC = []
	CsupplierP = []
	CcomponentP = []

	with open('TOTALALL.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',') 
		for row in readCSV:
			commodityP.append(row[0])
			commodityC.append(row[1])
			CsupplierP.append(row[2])
			CcomponentP.append(row[3])       

	i3 = 200000

	i = 0
	while i < len(commodity):
	    if commodity[i] == 'i3':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < i3:
	           i3 = j
	           i3supplier = supplier[i]
	           i3cost = int(cost[i])
	           k = 0
	           i3bestaval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'PROi3a':
	                   if i3bestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       i3besta = commodityC[k]
	                       i3bestaval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1      
	           k = 0
	           i3bestbval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'PROi3b':
	                   if i3bestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       i3bestb = commodityC[k]
	                       i3bestbval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1            
	                       
	           k = 0
	           i3bestcval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'PROi3c':
	                   if i3bestcval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       i3bestc = commodityC[k]
	                       i3bestcval = int(CsupplierP[k]) * int(CcomponentP[k])            
	               k = k+1
	    i = i+1

	i5 = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'i5':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < i5:
	           i5 = j
	           i5supplier = supplier[i]
	           i5cost = int(cost[i])
	           k = 0
	           i5bestaval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'PROi5a':
	                   if i5bestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       i5besta = commodityC[k]
	                       i5bestaval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1      
	           k = 0
	           i5bestbval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'PROi5b':
	                   if i5bestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       i5bestb = commodityC[k]
	                       i5bestbval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1            
	                       
	           k = 0
	           i5bestcval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'PROi5c':
	                   if i5bestcval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       i5bestc = commodityC[k]
	                       i5bestcval = int(CsupplierP[k]) * int(CcomponentP[k])            
	               k = k+1
	    i = i+1

	i7 = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'i7':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < i7:
	           i7 = j
	           i7supplier = supplier[i]
	           i7cost = int(cost[i])
	           k = 0
	           i7bestaval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'PROi7a':
	                   if i7bestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       i7besta = commodityC[k]
	                       i7bestaval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1      
	           k = 0
	           i7bestbval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'PROi7b':
	                   if i7bestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       i7bestb = commodityC[k]
	                       i7bestbval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1            
	                       
	           k = 0
	           i7bestcval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'PROi7c':
	                   if i7bestcval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       i7bestc = commodityC[k]
	                       i7bestcval = int(CsupplierP[k]) * int(CcomponentP[k])            
	               k = k+1
	    i = i+1

	i9 = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'i9':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < i9:
	           i9 = j
	           i9supplier = supplier[i]
	           i9cost = int(cost[i])
	           k = 0
	           i9bestaval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'PROi9a':
	                   if i9bestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       i9besta = commodityC[k]
	                       i9bestaval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1      
	           k = 0
	           i9bestbval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'PROi9b':
	                   if i9bestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       i9bestb = commodityC[k]
	                       i9bestbval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1            
	                       
	           k = 0
	           i9bestcval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'PROi9c':
	                   if i9bestcval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       i9bestc = commodityC[k]
	                       i9bestcval = int(CsupplierP[k]) * int(CcomponentP[k])            
	               k = k+1
	    i = i+1

	ram1gb = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'RAM 1GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < ram1gb:
	           ram1gb = j
	           ram1gbsupplier = supplier[i]
	           ram1gbcost = int(cost[i])
	           k = 0
	           ram1gbbestaval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'RAM1GBa':
	                   if ram1gbbestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       ram1gbbesta = commodityC[k]
	                       ram1gbbestaval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1      
	           k = 0
	           ram1gbbestbval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'RAM1GBb':
	                   if ram1gbbestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       ram1gbbestb = commodityC[k]
	                       ram1gbbestbval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1            
	                       
	           k = 0
	           ram1gbbestcval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'RAM1GBc':
	                   if ram1gbbestcval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       ram1gbbestc = commodityC[k]
	                       ram1gbbestcval = int(CsupplierP[k]) * int(CcomponentP[k])            
	               k = k+1
	    i = i+1

	ram2gb = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'RAM 2GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < ram2gb:
	           ram2gb = j
	           ram2gbsupplier = supplier[i]
	           ram2gbcost = int(cost[i])
	           k = 0
	           ram2gbbestaval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'RAM2GBa':
	                   if ram2gbbestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       ram2gbbesta = commodityC[k]
	                       ram2gbbestaval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1      
	           k = 0
	           ram2gbbestbval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'RAM2GBb':
	                   if ram2gbbestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       ram2gbbestb = commodityC[k]
	                       ram2gbbestbval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1            
	                       
	           k = 0
	           ram2gbbestcval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'RAM2GBc':
	                   if ram2gbbestcval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       ram2gbbestc = commodityC[k]
	                       ram2gbbestcval = int(CsupplierP[k]) * int(CcomponentP[k])            
	               k = k+1
	    i = i+1

	ram4gb = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'RAM 4GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < ram4gb:
	           ram4gb = j
	           ram4gbsupplier = supplier[i]
	           ram4gbcost = int(cost[i])
	           k = 0
	           ram4gbbestaval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'RAM4GBa':
	                   if ram4gbbestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       ram4gbbesta = commodityC[k]
	                       ram4gbbestaval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1      
	           k = 0
	           ram4gbbestbval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'RAM4GBb':
	                   if ram4gbbestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       ram4gbbestb = commodityC[k]
	                       ram4gbbestbval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1            
	                       
	           k = 0
	           ram4gbbestcval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'RAM4GBc':
	                   if ram4gbbestcval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       ram4gbbestc = commodityC[k]
	                       ram4gbbestcval = int(CsupplierP[k]) * int(CcomponentP[k])            
	               k = k+1
	    i = i+1

	ram8gb = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'RAM 8GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < ram8gb:
	           ram8gb = j
	           ram8gbsupplier = supplier[i]
	           ram8gbcost = int(cost[i])
	           k = 0
	           ram8gbbestaval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'RAM8GBa':
	                   if ram8gbbestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       ram8gbbesta = commodityC[k]
	                       ram8gbbestaval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1      
	           k = 0
	           ram8gbbestbval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'RAM8GBb':
	                   if ram8gbbestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       ram8gbbestb = commodityC[k]
	                       ram8gbbestbval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1            
	                       
	           k = 0
	           ram8gbbestcval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'RAM8GBc':
	                   if ram8gbbestcval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       ram8gbbestc = commodityC[k]
	                       ram8gbbestcval = int(CsupplierP[k]) * int(CcomponentP[k])            
	               k = k+1
	    i = i+1

	keyboardS = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'KEEYBOARD SIMPLE':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < keyboardS:
	           keyboardS = j
	           keyboardSsupplier = supplier[i]
	           keyboardScost = int(cost[i])
	    i = i+1

	keyboardBL = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'KEYBOARF BACKLIT':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < keyboardBL:
	           keyboardBL = j
	           keyboardBLsupplier = supplier[i]
	           keyboardBLcost = int(cost[i])
	    i = i+1

	keyboardST = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'KEYBOARD SOFT TOUCH':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < keyboardST:
	           keyboardST = j
	           keyboardSTsupplier = supplier[i]
	           keyboardSTcost = int(cost[i])
	    i = i+1

	screen23 = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'SCREEN 23':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < screen23:
	           screen23 = j
	           screen23supplier = supplier[i]
	           screen23cost = int(cost[i])
	    i = i+1

	screen24 = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'SCREEN 24':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < screen24:
	           screen24 = j
	           screen24supplier = supplier[i]
	           screen24cost = int(cost[i])
	    i = i+1

	screen27 = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'SCREEN 27':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < screen27:
	           screen27 = j
	           screen27supplier = supplier[i]
	           screen27cost = int(cost[i])
	    i = i+1

	mouse3 = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'MOUSE 3 CLICK':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < mouse3:
	           mouse3 = j
	           mouse3supplier = supplier[i]
	           mouse3cost = int(cost[i])
	    i = i+1

	mouse5 = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'MOUSE 5 CLICK':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < mouse5:
	           mouse5 = j
	           mouse5supplier = supplier[i]
	           mouse5cost = int(cost[i])
	    i = i+1

	gc1gb = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'GRAPHIC CARD 1GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < gc1gb:
	           gc1gb = j
	           gc1gbsupplier = supplier[i]
	           gc1gbcost = int(cost[i])
	    i = i+1

	gc2gb = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'GRAPHIC CARD 2GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < gc2gb:
	           gc2gb = j
	           gc2gbsupplier = supplier[i]
	           gc2gbcost = int(cost[i])
	    i = i+1

	gc4gb = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'GRAPHIC CARD 4GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < gc4gb:
	           gc4gb = j
	           gc4gbsupplier = supplier[i]
	           gc4gbcost = int(cost[i])
	    i = i+1

	#gc8gb = 200000
	#i = 0
	#while i < len(commodity):
	#    if commodity[i] == 'GRAPHIC CARD 8GB':
	#       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	#       if j<gc8gb:
	#           gc8gb = j
	#           gc8gbsupplier = supplier[i]
	#           gc8gbcost = int(cost[i])
	#    i = i+1

	hdd500gb = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'HDD 500GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < hdd500gb:
	           hdd500gb = j
	           hdd500gbsupplier = supplier[i]
	           hdd500gbcost = int(cost[i])
	           k = 0
	           hdd500gbbestaval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'HDD500GBa':
	                   if hdd500gbbestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       hdd500gbbesta = commodityC[k]
	                       hdd500gbbestaval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1      
	           k = 0
	           hdd500gbbestbval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'HDD500GBb':
	                   if hdd500gbbestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       hdd500gbbestb = commodityC[k]
	                       hdd500gbbestbval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1            
	                       
	           k = 0
	           hdd500gbbestcval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'HDD500GBc':
	                   if hdd500gbbestcval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       hdd500gbbestc = commodityC[k]
	                       hdd500gbbestcval = int(CsupplierP[k]) * int(CcomponentP[k])            
	               k = k+1
	    i = i+1

	hdd1tb = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'HDD 1TB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < hdd1tb:
	           hdd1tb = j
	           hdd1tbsupplier = supplier[i]
	           hdd1tbcost = int(cost[i])
	           k = 0
	           hdd1tbbestaval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'HDD1TBa':
	                   if hdd1tbbestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       hdd1tbbesta = commodityC[k]
	                       hdd1tbbestaval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1      
	           k = 0
	           hdd1tbbestbval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'HDD1TBb':
	                   if hdd1tbbestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       hdd1tbbestb = commodityC[k]
	                       hdd1tbbestbval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1            
	                       
	           k = 0
	           hdd1tbbestcval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'HDD1TBc':
	                   if hdd1tbbestcval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       hdd1tbbestc = commodityC[k]
	                       hdd1tbbestcval = int(CsupplierP[k]) * int(CcomponentP[k])            
	               k = k+1
	    i = i+1

	hdd2tb = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'HDD 2TB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < hdd2tb:
	           hdd2tb = j
	           hdd2tbsupplier = supplier[i]
	           hdd2tbcost = int(cost[i])
	           k = 0
	           hdd2tbbestaval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'HDD2TBa':
	                   if hdd2tbbestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       hdd2tbbesta = commodityC[k]
	                       hdd2tbbestaval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1      
	           k = 0
	           hdd2tbbestbval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'HDD2TBb':
	                   if hdd2tbbestaval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       hdd2tbbestb = commodityC[k]
	                       hdd2tbbestbval = int(CsupplierP[k]) * int(CcomponentP[k])
	               k = k+1            
	                       
	           k = 0
	           hdd2tbbestcval = 0
	           while k < len(commodityP):
	               if commodityP[k] == 'HDD2TBc':
	                   if hdd2tbbestcval < int(CsupplierP[k]) * int(CcomponentP[k]):
	                       hdd2tbbestc = commodityC[k]
	                       hdd2tbbestcval = int(CsupplierP[k]) * int(CcomponentP[k])            
	               k = k+1
	    i = i+1

	money = 0

	#commision of dell
	#money = money - ((money*13)/100)

	if choosenprocessor == 'i9':

		choosenprocessorcompany = i9supplier
		finalprocessor = i9cost
		money = money + i9cost
		beata = i9besta
		bestb = i9bestb
		bestc = i9bestc
        
        

	elif choosenprocessor == 'i7':

		choosenprocessorcompany = i7supplier
		money = money + i7cost
		finalprocessor = i7cost
		besta = i7besta
		bestb = i7bestb
		bestc = i7bestc

	elif choosenprocessor == 'i5':

		choosenprocessorcompany = i5supplier
		money = money + i5cost
		finalprocessor = i5cost
		besta = i5besta
		bestb = i5bestb
		bestc = i5bestc

	elif choosenprocessor == 'i3':

		choosenprocessorcompany = i3supplier
		money = money + i3cost
		finalprocessor = i3cost
		besta = i3besta
		bestb = i3bestb
		bestc = i3bestc

	if choosenscreen == 'screen 27 inch':

		choosenscreencompany = screen27supplier
		money = money + screen27cost
		finalscreen = screen27cost


	elif choosenscreen == 'screen 24 inch':

		choosenscreencompany = screen24supplier
		money = money + screen24cost
		finalscreen = screen24cost

	elif choosenscreen == 'screen 23 inch':

		choosenscreencompany = screen23supplier
		money = money + screen23cost
		finalscreen = screen23cost

	if choosengc == 'Graphic card 4 GB':

		choosengccompany = gc4gbsupplier

		money = money + gc4gbcost
		finalgc = gc4gbcost

	elif choosengc == 'Graphic card 2 GB':

		choosengccompany = gc2gbsupplier

		money = money + gc2gbcost
		finalgc = gc2gbcost

	elif choosengc == 'Graphic card 1 GB':

		choosengccompany = gc1gbsupplier

		money = money + gc1gbcost
		finalgc = gc1gbcost

	if choosenhdd == 'HDD 2 TB':

		choosenhddcompany = hdd2tbsupplier

		money = money + hdd2tbcost
		finalhdd = hdd2tbcost
		finalahdd = hdd2tbbesta
		finalbhdd = hdd2tbbestb
		finalchdd = hdd2tbbestc

	elif choosenhdd == 'HDD 1 TB':

		choosenhddcompany = hdd1tbsupplier

		money = money + hdd1tbcost
		finalhdd = hdd1tbcost
		finalahdd = hdd1tbbesta
		finalbhdd = hdd1tbbestb
		finalchdd = hdd1tbbestc

	elif choosenhdd == 'HDD 500 GB':

		choosenhddcompany = hdd500gbsupplier

		money = money + hdd500gbcost
		finalhdd = hdd500gbcost
		finalahdd = hdd500gbbesta
		finalbhdd = hdd500gbbestb
		finalchdd = hdd500gbbestc

	if choosenram == 'RAM 8 GB':

		choosenramcompany = ram8gbsupplier

		money = money + ram8gbcost
		finalram = ram8gbcost
		finalaram = ram8gbbesta
		finalbram = ram8gbbestb
		finalcram = ram8gbbestc

	elif choosenram == 'RAM 4 GB':

		choosenramcompany = ram4gbsupplier

		money = money + ram4gbcost
		finalram = ram4gbcost
		finalaram = ram4gbbesta
		finalbram = ram4gbbestb
		finalcram = ram4gbbestc

	elif choosenram == 'RAM 2 GB':

		choosenramcompany = ram2gbsupplier

		money = money + ram2gbcost
		finalram = ram2gbcost
		finalaram = ram2gbbesta
		finalbram = ram2gbbestb
		finalcram = ram2gbbestc

	elif choosenram == 'RAM 1 GB':

		choosenramcompany = ram1gbsupplier

		money = money + ram1gbcost
		finalram = ram1gbcost
		finalaram = ram1gbbesta
		finalbram = ram1gbbestb
		finalcram = ram1gbbestc

	if choosenkeyboard == 'KEYBOARD Soft Touch':

		choosenkeyboardcompany = keyboardSTsupplier
		money = money + keyboardSTcost
		finalkeyboard = keyboardSTcost

	elif choosenkeyboard == 'KEYBOARD Backlit':

		choosenkeyboardcompany = keyboardBLsupplier
		money = money + keyboardBLcost
		finalkeyboard = keyboardBLcost

	elif choosenkeyboard == 'KEYBOARD Simple':

	    choosenkeyboardcompany = keyboardSsupplier
	    money = money + keyboardScost
	    finalkeyboard = keyboardScost

	if choosenmouse == 'MOUSE 5 Click':

	    choosenmousecompany = mouse5supplier

	    money = money + mouse5cost
	    finalmouse = mouse5cost

	elif choosenmouse == 'MOUSE 3 Click':

	    choosenmousecompany = mouse3supplier

	    money = money + mouse3cost
	    finalmouse = mouse3cost

	return {'data': [{
            'processor':
            {
                'vendor': choosenprocessorcompany,
                'cost': finalprocessor,
                'besta': besta,
                'bestb': bestb,
                'bestc': bestc
            },
            'ram':
            {
                'vendor': choosenramcompany,
                'cost':finalram,
                'besta': finalaram,
                'bestb': finalbram,
                'bestc': finalcram


            },
            'hdd':
            {
                'vendor': choosenhddcompany,
                'cost':finalhdd,
                'besta': finalahdd,
                'bestb': finalbhdd,
                'bestc': finalchdd
            },
            'graphicscard':
            {
                'vendor': choosengccompany,
                'cost':finalgc
            },
            'mouse':
            {
                'vendor': choosenmousecompany,
                'cost':finalmouse
            },
            'screen':
            {
                'vendor': choosenscreencompany,
                'cost':finalscreen
            },
            'keyboard':
            {
                'vendor': choosenkeyboardcompany,
                'cost':finalkeyboard
            },
        }, {'cost': int(money)}, {'supplierreliability': randrange(65,80)}, {'componenetperformance': randrange(65,80)}
        ],
            'requeststatus': 'Success'}


def calculateCostOfDesktop(gc, hdd, keyboard, mouse, processor, ram, screen):
		
	choosenprocessor = processor
	
	choosenram = 'RAM '+ram
	
	choosenkeyboard = 'KEYBOARD '+keyboard
	
	choosenscreen = 'screen '+screen
	
	choosenmouse = 'MOUSE '+mouse
	
	choosenhdd = 'HDD '+hdd
	
	choosengc = 'Graphic card '+gc

	commodity = []
	component = []
	supplier = []
	cost = []
	supplierP = []
	componentP = []
	#with open('faban.txt') as fobj:
	#    for line in fobj:
	#        row = line.split()
	#        data.append(row[:-1])
	#        target.append(row[-1])

	with open('dataset.csv') as csvfile:
	    readCSV = csv.reader(csvfile, delimiter=',')
	    for row in readCSV:
	        commodity.append(row[0])
	        component.append(row[1])
	        supplier.append(row[2])
	        cost.append(row[3])
	        supplierP.append(row[4])
	        componentP.append(row[5])

	i3 = 200000

	i = 0
	while i < len(commodity):
	    if commodity[i] == 'i3':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < i3:
	           i3 = j
	           i3supplier = supplier[i]
	           i3cost = int(cost[i])
	    i = i+1

	i5 = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'i5':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < i5:
	           i5 = j
	           i5supplier = supplier[i]
	           i5cost = int(cost[i])
	    i = i+1

	i7 = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'i7':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < i7:
	           i7 = j
	           i7supplier = supplier[i]
	           i7cost = int(cost[i])
	    i = i+1

	i9 = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'i9':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < i9:
	           i9 = j
	           i9supplier = supplier[i]
	           i9cost = int(cost[i])
	    i = i+1

	ram1gb = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'RAM 1GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < ram1gb:
	           ram1gb = j
	           ram1gbsupplier = supplier[i]
	           ram1gbcost = int(cost[i])
	    i = i+1

	ram2gb = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'RAM 2GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < ram2gb:
	           ram2gb = j
	           ram2gbsupplier = supplier[i]
	           ram2gbcost = int(cost[i])
	    i = i+1

	ram4gb = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'RAM 4GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < ram4gb:
	           ram4gb = j
	           ram4gbsupplier = supplier[i]
	           ram4gbcost = int(cost[i])
	    i = i+1

	ram8gb = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'RAM 8GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < ram8gb:
	           ram8gb = j
	           ram8gbsupplier = supplier[i]
	           ram8gbcost = int(cost[i])
	    i = i+1

	keyboardS = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'KEEYBOARD SIMPLE':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < keyboardS:
	           keyboardS = j
	           keyboardSsupplier = supplier[i]
	           keyboardScost = int(cost[i])
	    i = i+1

	keyboardBL = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'KEYBOARF BACKLIT':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < keyboardBL:
	           keyboardBL = j
	           keyboardBLsupplier = supplier[i]
	           keyboardBLcost = int(cost[i])
	    i = i+1

	keyboardST = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'KEYBOARD SOFT TOUCH':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < keyboardST:
	           keyboardST = j
	           keyboardSTsupplier = supplier[i]
	           keyboardSTcost = int(cost[i])
	    i = i+1

	screen23 = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'SCREEN 23':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < screen23:
	           screen23 = j
	           screen23supplier = supplier[i]
	           screen23cost = int(cost[i])
	    i = i+1

	screen24 = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'SCREEN 24':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < screen24:
	           screen24 = j
	           screen24supplier = supplier[i]
	           screen24cost = int(cost[i])
	    i = i+1

	screen27 = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'SCREEN 27':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < screen27:
	           screen27 = j
	           screen27supplier = supplier[i]
	           screen27cost = int(cost[i])
	    i = i+1

	mouse3 = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'MOUSE 3 CLICK':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < mouse3:
	           mouse3 = j
	           mouse3supplier = supplier[i]
	           mouse3cost = int(cost[i])
	    i = i+1

	mouse5 = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'MOUSE 5 CLICK':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < mouse5:
	           mouse5 = j
	           mouse5supplier = supplier[i]
	           mouse5cost = int(cost[i])
	    i = i+1

	gc1gb = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'GRAPHIC CARD 1GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < gc1gb:
	           gc1gb = j
	           gc1gbsupplier = supplier[i]
	           gc1gbcost = int(cost[i])
	    i = i+1

	gc2gb = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'GRAPHIC CARD 2GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < gc2gb:
	           gc2gb = j
	           gc2gbsupplier = supplier[i]
	           gc2gbcost = int(cost[i])
	    i = i+1

	gc4gb = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'GRAPHIC CARD 4GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < gc4gb:
	           gc4gb = j
	           gc4gbsupplier = supplier[i]
	           gc4gbcost = int(cost[i])
	    i = i+1

	#gc8gb = 200000
	#i = 0
	#while i < len(commodity):
	#    if commodity[i] == 'GRAPHIC CARD 8GB':
	#       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	#       if j<gc8gb:
	#           gc8gb = j
	#           gc8gbsupplier = supplier[i]
	#           gc8gbcost = int(cost[i])
	#    i = i+1

	hdd500gb = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'HDD 500GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < hdd500gb:
	           hdd500gb = j
	           hdd500gbsupplier = supplier[i]
	           hdd500gbcost = int(cost[i])
	    i = i+1

	hdd1tb = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'HDD 1TB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < hdd1tb:
	           hdd1tb = j
	           hdd1tbsupplier = supplier[i]
	           hdd1tbcost = int(cost[i])
	    i = i+1

	hdd2tb = 200000
	i = 0
	while i < len(commodity):
	    if commodity[i] == 'HDD 2TB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j < hdd2tb:
	           hdd2tb = j
	           hdd2tbsupplier = supplier[i]
	           hdd2tbcost = int(cost[i])
	    i = i+1

	money = 0

	#commision of dell
	#money = money - ((money*13)/100)

	if choosenprocessor == 'i9':

		choosenprocessorcompany = i9supplier
		finalprocessor = i9cost
		money = money + i9cost
        
        

	elif choosenprocessor == 'i7':

		choosenprocessorcompany = i7supplier
		money = money + i7cost
		finalprocessor = i7cost

	elif choosenprocessor == 'i5':

		choosenprocessorcompany = i5supplier
		money = money + i5cost
		finalprocessor = i5cost

	elif choosenprocessor == 'i3':

		choosenprocessorcompany = i3supplier
		money = money + i3cost
		finalprocessor = i3cost

	if choosenscreen == 'screen 27 inch':

		choosenscreencompany = screen27supplier
		money = money + screen27cost
		finalscreen = screen27cost

	elif choosenscreen == 'screen 24 inch':

		choosenscreencompany = screen24supplier
		money = money + screen24cost
		finalscreen = screen24cost

	elif choosenscreen == 'screen 23 inch':

		choosenscreencompany = screen23supplier
		money = money + screen23cost
		finalscreen = screen23cost

	if choosengc == 'Graphic card 4 GB':

		choosengccompany = gc4gbsupplier

		money = money + gc4gbcost
		finalgc = gc4gbcost

	elif choosengc == 'Graphic card 2 GB':

		choosengccompany = gc2gbsupplier

		money = money + gc2gbcost
		finalgc = gc2gbcost

	elif choosengc == 'Graphic card 1 GB':

		choosengccompany = gc1gbsupplier

		money = money + gc1gbcost
		finalgc = gc1gbcost

	if choosenhdd == 'HDD 2 TB':

		choosenhddcompany = hdd2tbsupplier

		money = money + hdd2tbcost
		finalhdd = hdd2tbcost

	elif choosenhdd == 'HDD 1 TB':

		choosenhddcompany = hdd1tbsupplier

		money = money + hdd1tbcost
		finalhdd = hdd1tbcost

	elif choosenhdd == 'HDD 500 GB':

		choosenhddcompany = hdd500gbsupplier

		money = money + hdd500gbcost
		finalhdd = hdd500gbcost

	if choosenram == 'RAM 8 GB':

		choosenramcompany = ram8gbsupplier

		money = money + ram8gbcost
		finalram = ram8gbcost

	elif choosenram == 'RAM 4 GB':

		choosenramcompany = ram4gbsupplier

		money = money + ram4gbcost
		finalram = ram4gbcost

	elif choosenram == 'RAM 2 GB':

		choosenramcompany = ram2gbsupplier

		money = money + ram2gbcost
		finalram = ram2gbcost

	elif choosenram == 'RAM 1 GB':

		choosenramcompany = ram1gbsupplier

		money = money + ram1gbcost
		finalram = ram1gbcost

	if choosenkeyboard == 'KEYBOARD Soft Touch':

		choosenkeyboardcompany = keyboardSTsupplier
		money = money + keyboardSTcost
		finalkeyboard = keyboardSTcost

	elif choosenkeyboard == 'KEYBOARD Backlit':

		choosenkeyboardcompany = keyboardBLsupplier
		money = money + keyboardBLcost
		finalkeyboard = keyboardBLcost

	elif choosenkeyboard == 'KEYBOARD Simple':

	    choosenkeyboardcompany = keyboardSsupplier
	    money = money + keyboardScost
	    finalkeyboard = keyboardScost

	if choosenmouse == 'MOUSE 5 Click':

	    choosenmousecompany = mouse5supplier

	    money = money + mouse5cost
	    finalmouse = mouse5cost

	elif choosenmouse == 'MOUSE 3 Click':

	    choosenmousecompany = mouse3supplier

	    money = money + mouse3cost
	    finalmouse = mouse3cost

	return {'data': [{
            'processor':
            {
                'vendor': choosenprocessorcompany,
                'cost': finalprocessor
            },
            'ram':
            {
                'vendor': choosenramcompany,
                'cost':finalram

            },
            'hdd':
            {
                'vendor': choosenhddcompany,
                'cost':finalhdd
            },
            'graphicscard':
            {
                'vendor': choosengccompany,
                'cost':finalgc
            },
            'mouse':
            {
                'vendor': choosenmousecompany,
                'cost':finalmouse
            },
            'screen':
            {
                'vendor': choosenscreencompany,
                'cost':finalscreen
            },
            'keyboard':
            {
                'vendor': choosenkeyboardcompany,
                'cost':finalkeyboard
            },
        }, {'cost': int(money)}, {'supplierreliability': randrange(65,80)}, {'componenetperformance': randrange(65,80)}
        ],
            'requeststatus': 'Success'}

def calculateConfig(givenmoney):
    # Importing the dataset
    #dataset = pd.read_csv('dataset.csv')
    commodity = []
    component = []
    supplier = []
	
    cost = []
	
    supplierP = []
	
    componentP = []
	#with open('faban.txt') as fobj:
	#    for line in fobj:
	#        row = line.split()
	#        data.append(row[:-1])
	#        target.append(row[-1])

	
    with open('dataset.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
	        commodity.append(row[0])
	        component.append(row[1])
	        supplier.append(row[2])
	        cost.append(row[3])
	        supplierP.append(row[4])
	        componentP.append(row[5])
	     
    #print commodity[1]
    i3 = 200000 
    i = 0
	
    while i < len(commodity): 
	    
        if commodity[i] == 'i3':
	       
           j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       
           if j<i3 :
	           
               i3 = j
	           
               i3supplier = supplier[i]
	           
               i3cost = int(cost[i])
	    
        i = i+1  
	    
	
    i5 = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'i5':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<i5 :
	           i5 = j
	           i5supplier = supplier[i]
	           i5cost = int(cost[i])
	    i = i+1    

	
    i7 = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'i7':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<i7 :
	           i7 = j
	           i7supplier = supplier[i]
	           i7cost = int(cost[i])
	    i = i+1  

	
    
    i9 = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'i9':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<i9 :
	           i9 = j
	           i9supplier = supplier[i]
	           i9cost = int(cost[i])
	    i = i+1

	
    ram1gb = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'RAM 1GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<ram1gb :
	           ram1gb = j
	           ram1gbsupplier = supplier[i]
	           ram1gbcost = int(cost[i])
	    i = i+1 

	
    ram2gb = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'RAM 2GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<ram2gb :
	           ram2gb = j
	           ram2gbsupplier = supplier[i]
	           ram2gbcost = int(cost[i])
	    i = i+1    
	    
	
    ram4gb = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'RAM 4GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<ram4gb :
	           ram4gb = j
	           ram4gbsupplier = supplier[i]
	           ram4gbcost = int(cost[i])
	    i = i+1     
	        
	
    ram8gb = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'RAM 8GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<ram8gb :
	           ram8gb = j
	           ram8gbsupplier = supplier[i]
	           ram8gbcost = int(cost[i])
	    i = i+1 

	
    keyboardS = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'KEEYBOARD SIMPLE':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<keyboardS :
	           keyboardS = j
	           keyboardSsupplier = supplier[i]
	           keyboardScost = int(cost[i])
	    i = i+1 

	
    keyboardBL = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'KEYBOARF BACKLIT':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<keyboardBL :
	           keyboardBL = j
	           keyboardBLsupplier = supplier[i]
	           keyboardBLcost = int(cost[i])
	    i = i+1  


	
    keyboardST = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'KEYBOARD SOFT TOUCH':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<keyboardST :
	           keyboardST = j
	           keyboardSTsupplier = supplier[i]
	           keyboardSTcost = int(cost[i])
	    i = i+1              
	        
	
    screen23 = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'SCREEN 23':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<screen23 :
	           screen23 = j
	           screen23supplier = supplier[i]
	           screen23cost = int(cost[i])
	    i = i+1    

	
    screen24 = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'SCREEN 24':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<screen24:
	           screen24 = j
	           screen24supplier = supplier[i]
	           screen24cost = int(cost[i])
	    i = i+1 

	
    screen27 = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'SCREEN 27':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<screen27:
	           screen27 = j
	           screen27supplier = supplier[i]
	           screen27cost = int(cost[i])
	    i = i+1

	
    mouse3 = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'MOUSE 3 CLICK':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<mouse3:
	           mouse3 = j
	           mouse3supplier = supplier[i]
	           mouse3cost = int(cost[i])
	    i = i+1  

	
    mouse5 = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'MOUSE 5 CLICK':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<mouse5:
	           mouse5 = j
	           mouse5supplier = supplier[i]
	           mouse5cost = int(cost[i])
	    i = i+1  

	
    gc1gb = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'GRAPHIC CARD 1GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<gc1gb:
	           gc1gb = j
	           gc1gbsupplier = supplier[i]
	           gc1gbcost = int(cost[i])
	    i = i+1 

	
    gc2gb = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'GRAPHIC CARD 2GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<gc2gb:
	           gc2gb = j
	           gc2gbsupplier = supplier[i]
	           gc2gbcost = int(cost[i])
	    i = i+1 

	
    gc4gb = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'GRAPHIC CARD 4GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<gc4gb:
	           gc4gb = j
	           gc4gbsupplier = supplier[i]
	           gc4gbcost = int(cost[i])
	    i = i+1 

	#gc8gb = 200000 
	#i = 0
	#while i < len(commodity): 
	#    if commodity[i] == 'GRAPHIC CARD 8GB':
	#       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	#       if j<gc8gb:
	#           gc8gb = j
	#           gc8gbsupplier = supplier[i]
	#           gc8gbcost = int(cost[i])
	#    i = i+1 

	
    hdd500gb = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'HDD 500GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<hdd500gb:
	           hdd500gb = j
	           hdd500gbsupplier = supplier[i]
	           hdd500gbcost = int(cost[i])
	    i = i+1

	
    hdd1tb = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'HDD 1TB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<hdd1tb:
	           hdd1tb = j
	           hdd1tbsupplier = supplier[i]
	           hdd1tbcost = int(cost[i])
	    i = i+1

	
    hdd2tb = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'HDD 2TB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<hdd2tb:
	           hdd2tb = j
	           hdd2tbsupplier = supplier[i]
	           hdd2tbcost = int(cost[i])
	    i = i+1       


	
    money = givenmoney

	#commision of dell
	#money = money - ((money*13)/100)   
	
    remmoney = money
    
    moneyforprocessor = ((money*30)/100)

	
    if i9cost<=moneyforprocessor:
	    choosenprocessor = 'i9'
	    choosenprocessorcompany = i9supplier
	    remmoney = remmoney - i9cost
	    finalprocessor = i9cost

	
    elif i7cost<=moneyforprocessor:
	    choosenprocessor = 'i7'
	    choosenprocessorcompany = i7supplier
	    remmoney = remmoney - i7cost
	    finalprocessor = i7cost
	    
	
    elif i5cost<=moneyforprocessor:
	    choosenprocessor = 'i5'
	    choosenprocessorcompany = i5supplier
	    remmoney = remmoney - i5cost
	    finalprocessor = i5cost

	
    elif int(i3cost)<=moneyforprocessor:
	    choosenprocessor = 'i3'
	    choosenprocessorcompany = i3supplier
	    remmoney = remmoney - i3cost  
	    finalprocessor = i3cost

	
    moneyforscreen = ((money*25)/100)

	
    if screen27cost<=moneyforscreen:
	    choosenscreen = '27 inch'
	    choosenscreencompany = screen27supplier
	    remmoney = remmoney - screen27cost
	    finalscreen = screen27cost
	    
	
    elif screen24cost<=moneyforscreen:
	    choosenscreen = '24 inch'
	    choosenscreencompany = screen24supplier
	    remmoney = remmoney - screen24cost
	    finalscreen = screen24cost

	
    elif screen23cost<=moneyforscreen:
	    choosenscreen = '23 inch'
	    choosenscreencompany = screen23supplier
	    remmoney = remmoney - screen23cost
	    finalscreen = screen23cost    

	
    moneyforgc = ((money*15)/100)

	
    if gc4gbcost<=moneyforgc:
	    choosengc = '4 GB'
	    choosengccompany = gc4gbsupplier
	    remmoney = remmoney - gc4gbcost  
	    finalgc = gc4gbcost

	
    elif gc2gbcost<=moneyforgc:
	    choosengc = '2 GB'
	    choosengccompany = gc2gbsupplier
	    remmoney = remmoney - gc2gbcost 
	    finalgc = gc2gbcost

	
    elif gc1gbcost<=moneyforgc:
	    choosengc = '1 GB'
	    choosengccompany = gc1gbsupplier
	    remmoney = remmoney - gc1gbcost
	    finalgc = gc1gbcost      

	
    moneyforhdd = ((money*8)/100)

	
    if hdd2tbcost<=moneyforhdd:
	    choosenhdd = '2 TB'
	    choosenhddcompany = hdd2tbsupplier
	    remmoney = remmoney - hdd2tbcost 
	    finalhdd = hdd2tbcost
	    
	
    elif hdd1tbcost<=moneyforhdd:
	    choosenhdd = '1 TB'
	    choosenhddcompany = hdd1tbsupplier
	    remmoney = remmoney - hdd1tbcost 
	    finalhdd = hdd1tbcost

	
    elif hdd500gbcost<=moneyforhdd:
	    choosenhdd = '500 GB'
	    choosenhddcompany = hdd500gbsupplier
	    remmoney = remmoney - hdd500gbcost 
	    finalhdd = hdd500gbcost

	
    moneyforram = ((money*4)/100)

	
    if ram8gbcost<=moneyforram:
	    choosenram = '8 GB'
	    choosenramcompany = ram8gbsupplier
	    remmoney = remmoney - ram8gbcost 
	    finalram = ram8gbcost

	
    elif ram4gbcost<=moneyforram:
	    choosenram = '4 GB'
	    choosenramcompany = ram4gbsupplier
	    remmoney = remmoney - ram4gbcost 
	    finalram = ram4gbcost

	
    elif ram2gbcost<=moneyforram:
	    choosenram = '2 GB'
	    choosenramcompany = ram2gbsupplier
	    remmoney = remmoney - ram2gbcost 
	    finalram = ram2gbcost

	
    elif ram1gbcost<=moneyforram:
	    choosenram = '1 GB'
	    choosenramcompany = ram1gbsupplier
	    remmoney = remmoney - ram1gbcost  
	    finalram = ram1gbcost
	    
	    
	
    moneyforkeyboard = ((money*3)/100)

	
    if keyboardSTcost<=moneyforkeyboard:
	    choosenkeyboard = 'Soft Touch'
	    choosenkeyboardcompany = keyboardSTsupplier
	    remmoney = remmoney - keyboardSTcost 
	    finalkeyboard = keyboardSTcost

	
    elif keyboardBLcost<=moneyforkeyboard:
	    choosenkeyboard = 'Backlit'
	    choosenkeyboardcompany = keyboardBLsupplier
	    remmoney = remmoney - keyboardBLcost  
	    finalkeyboard = keyboardBLcost

	
    elif keyboardScost<=moneyforkeyboard:
	    choosenkeyboard = 'Simple'
	    choosenkeyboardcompany = keyboardSsupplier
	    remmoney = remmoney - keyboardScost   
	    finalkeyboard = keyboardScost
	    
	
    moneyformouse = ((money*2)/100)

	
    if mouse5cost<=moneyformouse:
	    choosenmouse = '5 Touch'
	    choosenmousecompany = mouse5supplier
	    remmoney = remmoney - mouse5cost 
	    finalmouse = mouse5cost 
	    
	
    elif mouse3cost<=moneyformouse:
	    choosenmouse = '3 Touch'
	    choosenmousecompany = mouse3supplier
	    remmoney = remmoney - mouse3cost
	    finalmouse = mouse3cost   

	
    remmoney = remmoney - ((money*13/100))  

	  
	      






	
    if choosenprocessor=='i7' and remmoney >= (i9cost - i7cost):
	    choosenprocessor = 'i9'
	    choosenprocessorcompany = i9supplier
	    remmoney = remmoney - (i9cost-i7cost)
	    finalprocessor = i9cost

	
    elif choosenprocessor=='i5' and remmoney >= (i7cost - i5cost):
	    choosenprocessor = 'i7'
	    choosenprocessorcompany = i7supplier
	    remmoney = remmoney - (i7cost - i5cost)
	    finalprocessor = i7cost
	    
	
    elif choosenprocessor=='i3' and remmoney >= (i5cost - i3cost):
	    choosenprocessor = 'i5'
	    choosenprocessorcompany = i5supplier
	    remmoney = remmoney - (i5cost - i3cost)
	    finalprocessor = i5cost





	
    if choosenscreen == '24 inch' and remmoney >= (screen27cost - screen24cost):
	    choosenscreen = '27 inch'
	    choosenscreencompany = screen27supplier
	    remmoney = remmoney - (screen27cost - screen24cost)
	    finalscreen = screen27cost
	    
	
    elif choosenscreen == '23 inch' and remmoney >= (screen24cost - screen23cost):
	    choosenscreen = '24 inch'
	    choosenscreencompany = screen24supplier
	    remmoney = remmoney - (screen24cost - screen23cost)
	    finalscreen = screen24cost



	
    if choosengc == '2 GB' and remmoney >= (gc4gbcost - gc2gbcost):
	    choosengc = '4 GB'
	    choosengccompany = gc4gbsupplier
	    remmoney = remmoney - (gc4gbcost - gc2gbcost) 
	    finalgc = gc4gbcost

	
    elif choosengc == '1 GB' and remmoney >= (gc2gbcost - gc1gbcost):
	    choosengc = '2 GB'
	    choosengccompany = gc2gbsupplier
	    remmoney = remmoney - (gc2gbcost - gc1gbcost) 
	    finalgc = gc2gbcost
	    



	
    if choosenhdd == '1 TB' and remmoney>=(hdd2tbcost-hdd1tbcost):
	    choosenhdd = '2 TB'
	    choosenhddcompany = hdd2tbsupplier
	    remmoney = remmoney - (hdd2tbcost-hdd1tbcost)
	    finalhdd = hdd2tbcost
	    
	
    elif choosenhdd == '500 GB' and remmoney>=(hdd1tbcost-hdd500gbcost):
	    choosenhdd = '1 TB'
	    choosenhddcompany = hdd1tbsupplier
	    remmoney = remmoney - (hdd1tbcost-hdd500gbcost)
	    finalhdd = hdd1tbcost




	
    if choosenram == '4 GB' and remmoney>=(ram8gbcost - ram4gbcost):
	    choosenram = '8 GB'
	    choosenramcompany = ram8gbsupplier
	    remmoney = remmoney - (ram8gbcost - ram4gbcost)
	    finalram = ram8gbcost

	
    elif choosenram == '2 GB' and remmoney>=(ram4gbcost - ram2gbcost):
	    choosenram = '4 GB'
	    choosenramcompany = ram4gbsupplier
	    remmoney = remmoney - (ram4gbcost - ram2gbcost)
	    finalram = ram4gbcost

	
    elif choosenram == '1 GB' and remmoney>=(ram2gbcost - ram1gbcost):
	    choosenram = '2 GB'
	    choosenramcompany = ram2gbsupplier
	    remmoney = remmoney - (ram2gbcost - ram1gbcost) 
	    finalram = ram2gbcost


	    
	    

	
    if choosenkeyboard == 'Backlit' and remmoney>=(keyboardSTcost - keyboardBLcost):
	    choosenkeyboard = 'Soft Touch'
	    choosenkeyboardcompany = keyboardSTsupplier
	    remmoney = remmoney - (keyboardSTcost - keyboardBLcost) 
	    finalkeyboard = keyboardSTcost

	
    elif choosenkeyboard == 'Simple' and remmoney>=(keyboardBLcost - keyboardScost):
	    choosenkeyboard = 'Backlit'
	    choosenkeyboardcompany = keyboardBLsupplier
	    remmoney = remmoney - keyboardBLcost - keyboardScost
	    finalkeyboard = keyboardBLcost





	
    if choosenmouse == '3 Touch' and remmoney>=(mouse5cost - mouse3cost):
	    choosenmouse = '5 Touch'
	    choosenmousecompany = mouse5supplier
	    remmoney = remmoney - (mouse5cost - mouse3cost)  
	    finalmouse = mouse5cost
	    
	  

    
    return {'data': [
        {
            'processor':
            {
                'vendor': choosenprocessorcompany,
                'part': choosenprocessor,
                'cost':finalprocessor,
                'costa':'a2',
                'costb':'b2',
                'costc':'c3'

            },
            'ram':
            {
                'vendor': choosenramcompany,
                'part': choosenram,
                'cost':finalram,
                'costa':'a1',
                'costb':'b3',
                'costc':'c1'
            },
            'hdd':
            {
                'vendor': choosenhddcompany,
                'part': choosenhdd,
                'cost':finalhdd,
                'costa':'a3',
                'costb':'b1',
                'costc':'c2'
            },
            'graphicscard':
            {
                'vendor': choosengccompany,
                'part': choosengc,
                'cost':finalgc
            },
            'mouse':
            {
                'vendor': choosenmousecompany,
                'part': choosenmouse,
                'cost':finalmouse
            },
            'screen':
            {
                'vendor': choosenscreencompany,
                'part': choosenscreen,
                'cost':finalscreen
            },
            'keyboard':
            {
                'vendor': choosenkeyboardcompany,
                'part': choosenkeyboard,
                'cost':finalkeyboard
            },
        }, {'cost': int(remmoney)}, {'supplierreliability': randrange(60,80)}, {'componenetperformance': randrange(60,80)}
    ],
        'requeststatus': 'Success'}

def calculateConfigLaptop(givenmoney):
    # Importing the dataset
    #dataset = pd.read_csv('dataset.csv')
    commodity = []
    component = []
    supplier = []
	
    cost = []
	
    supplierP = []
	
    componentP = []
	#with open('faban.txt') as fobj:
	#    for line in fobj:
	#        row = line.split()
	#        data.append(row[:-1])
	#        target.append(row[-1])

	
    with open('dataset.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
	        commodity.append(row[0])
	        component.append(row[1])
	        supplier.append(row[2])
	        cost.append(row[3])
	        supplierP.append(row[4])
	        componentP.append(row[5])
	     
    #print commodity[1]
    i3 = 200000 
    i = 0
	
    while i < len(commodity): 
	    
        if commodity[i] == 'i3':
	       
           j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       
           if j<i3 :
	           
               i3 = j
	           
               i3supplier = supplier[i]
	           
               i3cost = int(cost[i])
	    
        i = i+1  
	    
	
    i5 = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'i5':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<i5 :
	           i5 = j
	           i5supplier = supplier[i]
	           i5cost = int(cost[i])
	    i = i+1    

	
    i7 = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'i7':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<i7 :
	           i7 = j
	           i7supplier = supplier[i]
	           i7cost = int(cost[i])
	    i = i+1  

	
    
    i9 = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'i9':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<i9 :
	           i9 = j
	           i9supplier = supplier[i]
	           i9cost = int(cost[i])
	    i = i+1

	
    ram1gb = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'RAM 1GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<ram1gb :
	           ram1gb = j
	           ram1gbsupplier = supplier[i]
	           ram1gbcost = int(cost[i])
	    i = i+1 

	
    ram2gb = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'RAM 2GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<ram2gb :
	           ram2gb = j
	           ram2gbsupplier = supplier[i]
	           ram2gbcost = int(cost[i])
	    i = i+1    
	    
	
    ram4gb = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'RAM 4GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<ram4gb :
	           ram4gb = j
	           ram4gbsupplier = supplier[i]
	           ram4gbcost = int(cost[i])
	    i = i+1     
	        
	
    ram8gb = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'RAM 8GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<ram8gb :
	           ram8gb = j
	           ram8gbsupplier = supplier[i]
	           ram8gbcost = int(cost[i])
	    i = i+1 

	
    keyboardS = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'KEEYBOARD SIMPLE':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<keyboardS :
	           keyboardS = j
	           keyboardSsupplier = supplier[i]
	           keyboardScost = int(cost[i])
	    i = i+1 

	
    keyboardBL = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'KEYBOARF BACKLIT':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<keyboardBL :
	           keyboardBL = j
	           keyboardBLsupplier = supplier[i]
	           keyboardBLcost = int(cost[i])
	    i = i+1  


	
    keyboardST = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'KEYBOARD SOFT TOUCH':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<keyboardST :
	           keyboardST = j
	           keyboardSTsupplier = supplier[i]
	           keyboardSTcost = int(cost[i])
	    i = i+1              
	        
	
    screen23 = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'SCREEN 23':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<screen23 :
	           screen23 = j
	           screen23supplier = supplier[i]
	           screen23cost = int(cost[i])
	    i = i+1    

	
    screen24 = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'SCREEN 24':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<screen24:
	           screen24 = j
	           screen24supplier = supplier[i]
	           screen24cost = int(cost[i])
	    i = i+1 

	
    screen27 = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'SCREEN 27':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<screen27:
	           screen27 = j
	           screen27supplier = supplier[i]
	           screen27cost = int(cost[i])
	    i = i+1

	
    mouse3 = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'MOUSE 3 CLICK':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<mouse3:
	           mouse3 = j
	           mouse3supplier = supplier[i]
	           mouse3cost = int(cost[i])
	    i = i+1  

	
    mouse5 = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'MOUSE 5 CLICK':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<mouse5:
	           mouse5 = j
	           mouse5supplier = supplier[i]
	           mouse5cost = int(cost[i])
	    i = i+1  

	
    gc1gb = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'GRAPHIC CARD 1GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<gc1gb:
	           gc1gb = j
	           gc1gbsupplier = supplier[i]
	           gc1gbcost = int(cost[i])
	    i = i+1 

	
    gc2gb = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'GRAPHIC CARD 2GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<gc2gb:
	           gc2gb = j
	           gc2gbsupplier = supplier[i]
	           gc2gbcost = int(cost[i])
	    i = i+1 

	
    gc4gb = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'GRAPHIC CARD 4GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<gc4gb:
	           gc4gb = j
	           gc4gbsupplier = supplier[i]
	           gc4gbcost = int(cost[i])
	    i = i+1 

	#gc8gb = 200000 
	#i = 0
	#while i < len(commodity): 
	#    if commodity[i] == 'GRAPHIC CARD 8GB':
	#       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	#       if j<gc8gb:
	#           gc8gb = j
	#           gc8gbsupplier = supplier[i]
	#           gc8gbcost = int(cost[i])
	#    i = i+1 

	
    hdd500gb = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'HDD 500GB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<hdd500gb:
	           hdd500gb = j
	           hdd500gbsupplier = supplier[i]
	           hdd500gbcost = int(cost[i])
	    i = i+1

	
    hdd1tb = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'HDD 1TB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<hdd1tb:
	           hdd1tb = j
	           hdd1tbsupplier = supplier[i]
	           hdd1tbcost = int(cost[i])
	    i = i+1

	
    hdd2tb = 200000 
	
    i = 0
	
    while i < len(commodity): 
	    if commodity[i] == 'HDD 2TB':
	       j = int(cost[i]) * (1/int(supplierP[i])) * (1/int(componentP[i]))
	       if j<hdd2tb:
	           hdd2tb = j
	           hdd2tbsupplier = supplier[i]
	           hdd2tbcost = int(cost[i])
	    i = i+1       


	
    money = givenmoney

	#commision of dell
	#money = money - ((money*13)/100)   
	
    remmoney = money
    
    moneyforprocessor = ((money*30)/100)

	
    if i9cost<=moneyforprocessor:
	    choosenprocessor = 'i9'
	    choosenprocessorcompany = i9supplier
	    remmoney = remmoney - i9cost
	    finalprocessor = i9cost

	
    elif i7cost<=moneyforprocessor:
	    choosenprocessor = 'i7'
	    choosenprocessorcompany = i7supplier
	    remmoney = remmoney - i7cost
	    finalprocessor = i7cost
	    
	
    elif i5cost<=moneyforprocessor:
	    choosenprocessor = 'i5'
	    choosenprocessorcompany = i5supplier
	    remmoney = remmoney - i5cost
	    finalprocessor = i5cost

	
    elif int(i3cost)<=moneyforprocessor:
	    choosenprocessor = 'i3'
	    choosenprocessorcompany = i3supplier
	    remmoney = remmoney - i3cost  
	    finalprocessor = i3cost

	
    moneyforscreen = ((money*25)/100)

	
    if screen27cost<=moneyforscreen:
	    choosenscreen = '27 inch'
	    choosenscreencompany = screen27supplier
	    remmoney = remmoney - screen27cost
	    finalscreen = screen27cost
	    
	
    elif screen24cost<=moneyforscreen:
	    choosenscreen = '24 inch'
	    choosenscreencompany = screen24supplier
	    remmoney = remmoney - screen24cost
	    finalscreen = screen24cost

	
    elif screen23cost<=moneyforscreen:
	    choosenscreen = '23 inch'
	    choosenscreencompany = screen23supplier
	    remmoney = remmoney - screen23cost
	    finalscreen = screen23cost    

	
    moneyforgc = ((money*15)/100)

	
    if gc4gbcost<=moneyforgc:
	    choosengc = '4 GB'
	    choosengccompany = gc4gbsupplier
	    remmoney = remmoney - gc4gbcost  
	    finalgc = gc4gbcost

	
    elif gc2gbcost<=moneyforgc:
	    choosengc = '2 GB'
	    choosengccompany = gc2gbsupplier
	    remmoney = remmoney - gc2gbcost 
	    finalgc = gc2gbcost

	
    elif gc1gbcost<=moneyforgc:
	    choosengc = '1 GB'
	    choosengccompany = gc1gbsupplier
	    remmoney = remmoney - gc1gbcost
	    finalgc = gc1gbcost      

	
    moneyforhdd = ((money*8)/100)

	
    if hdd2tbcost<=moneyforhdd:
	    choosenhdd = '2 TB'
	    choosenhddcompany = hdd2tbsupplier
	    remmoney = remmoney - hdd2tbcost 
	    finalhdd = hdd2tbcost
	    
	
    elif hdd1tbcost<=moneyforhdd:
	    choosenhdd = '1 TB'
	    choosenhddcompany = hdd1tbsupplier
	    remmoney = remmoney - hdd1tbcost 
	    finalhdd = hdd1tbcost

	
    elif hdd500gbcost<=moneyforhdd:
	    choosenhdd = '500 GB'
	    choosenhddcompany = hdd500gbsupplier
	    remmoney = remmoney - hdd500gbcost 
	    finalhdd = hdd500gbcost

	
    moneyforram = ((money*4)/100)

	
    if ram8gbcost<=moneyforram:
	    choosenram = '8 GB'
	    choosenramcompany = ram8gbsupplier
	    remmoney = remmoney - ram8gbcost 
	    finalram = ram8gbcost

	
    elif ram4gbcost<=moneyforram:
	    choosenram = '4 GB'
	    choosenramcompany = ram4gbsupplier
	    remmoney = remmoney - ram4gbcost 
	    finalram = ram4gbcost

	
    elif ram2gbcost<=moneyforram:
	    choosenram = '2 GB'
	    choosenramcompany = ram2gbsupplier
	    remmoney = remmoney - ram2gbcost 
	    finalram = ram2gbcost

	
    elif ram1gbcost<=moneyforram:
	    choosenram = '1 GB'
	    choosenramcompany = ram1gbsupplier
	    remmoney = remmoney - ram1gbcost  
	    finalram = ram1gbcost
	    
	    
	
    moneyforkeyboard = ((money*3)/100)

	
    if keyboardSTcost<=moneyforkeyboard:
	    choosenkeyboard = 'Soft Touch'
	    choosenkeyboardcompany = keyboardSTsupplier
	    remmoney = remmoney - keyboardSTcost 
	    finalkeyboard = keyboardSTcost

	
    elif keyboardBLcost<=moneyforkeyboard:
	    choosenkeyboard = 'Backlit'
	    choosenkeyboardcompany = keyboardBLsupplier
	    remmoney = remmoney - keyboardBLcost  
	    finalkeyboard = keyboardBLcost

	
    elif keyboardScost<=moneyforkeyboard:
	    choosenkeyboard = 'Simple'
	    choosenkeyboardcompany = keyboardSsupplier
	    remmoney = remmoney - keyboardScost   
	    finalkeyboard = keyboardScost
	    
	
    moneyformouse = ((money*2)/100)

	
    if mouse5cost<=moneyformouse:
	    choosenmouse = 'Buttonless'
	    choosenmousecompany = mouse5supplier
	    remmoney = remmoney - mouse5cost 
	    finalmouse = mouse5cost 
	    
	
    elif mouse3cost<=moneyformouse:
	    choosenmouse = 'Traditional'
	    choosenmousecompany = mouse3supplier
	    remmoney = remmoney - mouse3cost
	    finalmouse = mouse3cost   

	
    remmoney = remmoney - ((money*13/100))  

	  
	      






	
    if choosenprocessor=='i7' and remmoney >= (i9cost - i7cost):
	    choosenprocessor = 'i9'
	    choosenprocessorcompany = i9supplier
	    remmoney = remmoney - (i9cost-i7cost)
	    finalprocessor = i9cost

	
    elif choosenprocessor=='i5' and remmoney >= (i7cost - i5cost):
	    choosenprocessor = 'i7'
	    choosenprocessorcompany = i7supplier
	    remmoney = remmoney - (i7cost - i5cost)
	    finalprocessor = i7cost
	    
	
    elif choosenprocessor=='i3' and remmoney >= (i5cost - i3cost):
	    choosenprocessor = 'i5'
	    choosenprocessorcompany = i5supplier
	    remmoney = remmoney - (i5cost - i3cost)
	    finalprocessor = i5cost





	
    if choosenscreen == '24 inch' and remmoney >= (screen27cost - screen24cost):
	    choosenscreen = '27 inch'
	    choosenscreencompany = screen27supplier
	    remmoney = remmoney - (screen27cost - screen24cost)
	    finalscreen = screen27cost
	    
	
    elif choosenscreen == '23 inch' and remmoney >= (screen24cost - screen23cost):
	    choosenscreen = '24 inch'
	    choosenscreencompany = screen24supplier
	    remmoney = remmoney - (screen24cost - screen23cost)
	    finalscreen = screen24cost



	
    if choosengc == '2 GB' and remmoney >= (gc4gbcost - gc2gbcost):
	    choosengc = '4 GB'
	    choosengccompany = gc4gbsupplier
	    remmoney = remmoney - (gc4gbcost - gc2gbcost) 
	    finalgc = gc4gbcost

	
    elif choosengc == '1 GB' and remmoney >= (gc2gbcost - gc1gbcost):
	    choosengc = '2 GB'
	    choosengccompany = gc2gbsupplier
	    remmoney = remmoney - (gc2gbcost - gc1gbcost) 
	    finalgc = gc2gbcost
	    



	
    if choosenhdd == '1 TB' and remmoney>=(hdd2tbcost-hdd1tbcost):
	    choosenhdd = '2 TB'
	    choosenhddcompany = hdd2tbsupplier
	    remmoney = remmoney - (hdd2tbcost-hdd1tbcost)
	    finalhdd = hdd2tbcost
	    
	
    elif choosenhdd == '500 GB' and remmoney>=(hdd1tbcost-hdd500gbcost):
	    choosenhdd = '1 TB'
	    choosenhddcompany = hdd1tbsupplier
	    remmoney = remmoney - (hdd1tbcost-hdd500gbcost)
	    finalhdd = hdd1tbcost




	
    if choosenram == '4 GB' and remmoney>=(ram8gbcost - ram4gbcost):
	    choosenram = '8 GB'
	    choosenramcompany = ram8gbsupplier
	    remmoney = remmoney - (ram8gbcost - ram4gbcost)
	    finalram = ram8gbcost

	
    elif choosenram == '2 GB' and remmoney>=(ram4gbcost - ram2gbcost):
	    choosenram = '4 GB'
	    choosenramcompany = ram4gbsupplier
	    remmoney = remmoney - (ram4gbcost - ram2gbcost)
	    finalram = ram4gbcost

	
    elif choosenram == '1 GB' and remmoney>=(ram2gbcost - ram1gbcost):
	    choosenram = '2 GB'
	    choosenramcompany = ram2gbsupplier
	    remmoney = remmoney - (ram2gbcost - ram1gbcost) 
	    finalram = ram2gbcost


	    
	    

	
    if choosenkeyboard == 'Backlit' and remmoney>=(keyboardSTcost - keyboardBLcost):
	    choosenkeyboard = 'Soft Touch'
	    choosenkeyboardcompany = keyboardSTsupplier
	    remmoney = remmoney - (keyboardSTcost - keyboardBLcost) 
	    finalkeyboard = keyboardSTcost

	
    elif choosenkeyboard == 'Simple' and remmoney>=(keyboardBLcost - keyboardScost):
	    choosenkeyboard = 'Backlit'
	    choosenkeyboardcompany = keyboardBLsupplier
	    remmoney = remmoney - keyboardBLcost - keyboardScost
	    finalkeyboard = keyboardBLcost





	
    if choosenmouse == 'Traditional' and remmoney>=(mouse5cost - mouse3cost):
	    choosenmouse = 'Buttonless'
	    choosenmousecompany = mouse5supplier
	    remmoney = remmoney - (mouse5cost - mouse3cost)  
	    finalmouse = mouse5cost
	    
	  

    
    return {'data': [
        {
            'processor':
            {
                'vendor': choosenprocessorcompany,
                'part': choosenprocessor,
                'cost':finalprocessor,
                'costa':'a3',
                'costb':'b2',
                'costc':'c2' 

            },
            'ram':
            {
                'vendor': choosenramcompany,
                'part': choosenram,
                'cost':finalram,
                'costa':'a1',
                'costb':'b3',
                'costc':'c1'
            },
            'hdd':
            {
                'vendor': choosenhddcompany,
                'part': choosenhdd,
                'cost':finalhdd,
                'costa':'a2',
                'costb':'b1',
                'costc':'c1'
            },
            'graphicscard':
            {
                'vendor': choosengccompany,
                'part': choosengc,
                'cost':finalgc
            },
            'mouse':
            {
                'vendor': choosenmousecompany,
                'part': choosenmouse,
                'cost':finalmouse
            },
            'screen':
            {
                'vendor': choosenscreencompany,
                'part': choosenscreen,
                'cost':finalscreen
            },
            'keyboard':
            {
                'vendor': choosenkeyboardcompany,
                'part': choosenkeyboard,
                'cost':finalkeyboard
            },
        }, {'cost': int(remmoney)}, {'supplierreliability': randrange(60,80)}, {'componenetperformance': randrange(60,80)}
    ],
        'requeststatus': 'Success'}        
