# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 19:43:41 2022

@author: Amin Shakya
"""
import tkinter
import tkinter.messagebox as messagebox
# import os
def detect_person():
    import random
    import numpy as np
    return np.rint(random.uniform(0,1))

def detect_gloves():
    import random    
    import numpy as np
    return np.rint(random.uniform(0,1))


flag = list()
count = 0
threshold = 3
for i in range(100):
    if detect_gloves() == 0 and detect_person() == 1:
        flag.append(1)
        count = count+1
        if count>=threshold:
            messagebox.showwarning(title = 'PPE Non-compliance', message = 'Gloves not worn')
        
            
    else:
        flag.append(0)
        count = 0


    
