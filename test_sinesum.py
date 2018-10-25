#!/usr/bin/env python3

"""sinesum.py Test Module

Verify implementation of the Fourier sine series using numpy arrays.
"""

import numpy.testing as np
import sinesum

#def dummy_test:
#this test wasnt that helpufl
def test_ft():
    np.assert_approx_equal(sinesum .ft(2,-0.5), -1.0, significant = 2)
   
    np.assert_approx_equal(sinesum .ft(2,0), 0.0, significant=2)
    
    np.assert_approx_equal(sinesum .ft(2,0.5), 1.0, significant = 2)

def test_sn():
    np.assert_approx_equal(sinesum .sn(2,0,100), 0 , significant = 2)

    np.assert_approx_equal(sinesum .sn(2,0.5,100),1, significant = 2)
    
    np.assert_approx_equal(sinesum .sn(2,-0.5,100),-1, significant = 2)

