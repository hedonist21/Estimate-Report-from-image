#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 13:52:22 2019

@author: divyanshsingh
"""
keyfile = "keys.txt"
testfile = "st.txt"
fl= open('par.txt','r+')
tmp=""
keys = [key for key in (line.strip() for line in open(keyfile)) if key]
with open(testfile,'r') as f:
    for line in f:
        for key in keys:
            if key in line:
                if "SUBTOTAL" not in line: 
                    print(line, file= fl)
i=-1
foodtotal=0.0
gastotal=0.0
r='Restaurant'
t='TRUCK'
for line in fl:
    if r in line:
        print('1')
        i=1;
        continue
    if t in line:
        i=2
        continue
    tmp="".join([i for i in line if i=="." or i.isdigit() or i==','])
    if tmp!=''and i==1:
        print(tmp)
        val=float(tmp)
        print(str(val))
        foodtotal+=val
    if tmp!='' and i==2:
        print(tmp)
        val=float(tmp)
        print(str(val))
        gastotal+=val
    
        
print('food='+str(foodtotal))
print('gas='+str(gastotal))