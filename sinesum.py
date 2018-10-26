#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt



def ft(t,T=(2*np.pi)):
    if t>T/2 or t< -T/2:
        return exit(0) 
        print('t is not in the domain, please try again.')
    
    if t == 0:
        return 0
    if (t > 0) and (t < T/2):
        return 1
    if (t < 0) and (t > -T/2):
        return -1


def plotf(t, n, T=(2 * np.pi)):
 
    f = plots(t, n, T)
    plt.xlim(0, n)
    plt.grid()

    return plt.plot(f)

def sn(t,n,T=(2*np.pi)):
    k = 1
    a = 0
    sum1 = 0
    list1 = []
    while k !=n :
       # a = (4/np.pi)*((1/((2*k)-1)) * np.sin(((2*(2*k)-1)*np.pi * t)/T))
        a = (4/np.pi)*(1/(2*k-1))*(np.sin((2*(2*k-1)*np.pi*t)/(T)))
        sum1 = sum1 + a
        list1.append(sum1)
        k = k + 1
    return (sum1)

print(sn((np.pi),1000,(2*np.pi)))

def sn1(t, n, T=(2*np.pi)):
    k = np.arange(1 , n+1 , 1 )
    
    s = (1/(2*k-1))*(np.sin((2*(2*k-1)*np.pi*t)/(T)))
    
    return (4/np.pi)*np.sn1(s)


def plotsn(t, n, T=(2 * np.pi)):

    s = (4 / np.pi) * (1 / ((2 * k) - 1)) * np.sin((2 * ((2 * k) - 1) * np.pi * t)  / T)
    list1 = []
    for i in n+1:
        a = 0
        b = 0
        while a < i - 1:
            b = b + s[a]
            a= a+1
        list1.append(tot)

    return list1

