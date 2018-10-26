#!/usr/bin/env python3

"""sinesum.py Test Module

Verify implementation of the Fourier sine series using numpy arrays.
"""

import numpy as np
import sinesum
import math


"""In each one we just check for the ft function outputs -1 if x < 0 , 0 if x = 0, 1 if x > 0, and sn sum approximation """

def sn1():
 
    assert math.isclose(sinesum.sn(np.pi/2, 100000), 1.0, rel_tol=1e-5)

def ft1():
    assert sinesum.ft(np.pi/2) == 1

def ft2():
    assert sinesum.ft(0) == 0

def ft3():
    assert sinesum.ft(-np.pi/2) == -1
    

    
    
    

