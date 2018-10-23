#!/usr/bin/env python3

import numpy as np



def ft(t,T=(2*np.pi)):
    if t>T/2 or t< -T/2:
        return exit(0)
    
    if t == 0:
        return 0
    if (t > 0) and (t < T/2):
        return 1
    if (t < 0) and (t > -T/2):
        return -1

    
def sn(t,n,T=(2*np.pi)):
    k = 1
    a = 0
    sum1 = 0
    list1 = []
    while k !=n :
        a = (4/np.pi)*((1/((2*k)-1)) * np.sin(((2*(2*k)-1)*np.pi * t)/T))
        sum1 = sum1 + a
        list1.append(sum1)
        k = k + 1
    return (sum1)

print(sn((np.pi),1000,(2*np.pi)))
