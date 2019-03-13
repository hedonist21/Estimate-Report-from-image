#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 6 11:22:09 2019

@author: divyanshsingh
"""

from tesserocr import PyTessBaseAPI
images = ['sample-gas-receipt.jpg','george-s-italian-restaurant.jpg','blank-restaurant-receipt.jpg']
f= open('st.txt','r+')
with PyTessBaseAPI() as api:
    for img in images:
        api.SetImageFile(img)
        print (api.GetUTF8Text(), file=f)
        print ('-----------------------', file=f)
f.close()
