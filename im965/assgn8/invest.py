# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 15:52:39 2014

@author: Israel
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from myexceptions import *

def calcCumRet(bet):
    ''' Returns the cumulative value of 'bet' investments of value 1000/'bet' 
        in an instrument that returns double 51% and zero 49%  of the time'''
    return ((np.random.random((1,bet))>0.49).sum(axis=1)*2.0*(1000/bet))[0]

    
def invest(positions,num_trials):
    '''Returns a dataframe with percentage returns of the form [trial(i),position(j)], 
    where entry[i,j] represents the i'th independent trial of buying 'j' investments 
    of value 1000/'j' in an instrument the returns double 51% and zero 49%  of the time.'''
    
    #Exception Handling (positions argument)
    if type(positions)!=list:
        raise NotListError
    if all([(type(x)==int or type(x)==float) for x in positions])==False:
        raise NotNumError
    if all([x % 1==0.0 for x in positions])==False:
        raise NotIntError
    if all([(0<x<=1000) for x in positions])==False:
        raise InvalidPosError
        
    #Excption Handling (num_trials argument)    
    if (type(num_trials)!=int and type(num_trials)!=float):
        raise TrialNotNumError
    if 0>=(num_trials):
        raise TrialNegError
    
    #Program
    position_value = 1000/np.array(positions)
    cumu_ret = DataFrame(columns=positions,index=np.arange(1,num_trials+1))
    
    for i in position_value:
        col=1000/i
        cumu_ret[col] = col
        cumu_ret[col] = cumu_ret[col].map(calcCumRet)    
    daily_ret = (cumu_ret/1000)-1
    return daily_ret
