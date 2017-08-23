# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Plotting Methods

This module provides methods for various kinds of plots.

"""
from __future__ import division
import os
import numpy as np
import pandas as pd


import matplotlib.pyplot as plt
from matplotlib import rc

get_ipython().run_line_magic('matplotlib', 'inline')	
plt.style.use('classic')
plt.rc("figure", facecolor="white")
"""
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=4)
plt.rc('ytick', labelsize=4)
plt.rc('axes', labelsize=4)
rcParams.update({'figure.autolayout': True})
"""


 

 
rc('text', usetex=True)
plt.rcParams['text.latex.preamble'] = [
    r'\usepackage{tgheros}',    # helvetica font
    r'\usepackage{sansmath}',   # math-font matching  helvetica
    r'\sansmath'                # actually tell tex to use it!
    r'\usepackage{siunitx}',    # micro symbols
    r'\sisetup{detect-all}',    # force siunitx to use the fonts
]  
 
 
"""
t = np.arange(0.0, 1.0+0.01, 0.01)
s = np.cos(2*2*np.pi*t)+2
pl.plot(t, s)
 
 
pl.xlabel(r'time $\lambda$')
pl.ylabel(r'\textit{voltage (mV)}',fontsize=16)
pl.title(r'\TeX\ Number 1234567890 anisotropic ' +
         r'$\displaystyle\sum_{n=1}^\infty' +
         r'\frac{-e^{i\pi}}{2^n}$' +
         r' and \SI{3}{\micro\metre}',fontsize=16, color='r')
 
pl.grid(True)
pl.savefig('matplotlib_helvetica.pdf')
"""
width = 6.5
height = width / 1.618


def plot_consumption(figure_name, which_house, data):

	plt.figure(1, figsize=(6,4))
	plt.plot(data, color='b')
	
	plt.xticks(rotation=45)
	plt.title(r'House nr. '+str(which_house)+r' Electricity Consumption')
	plt.xlabel(r'Time')
	plt.ylabel(r'Consumption (kwh)')
	plt.grid(True)
	plt.show()
	plt.savefig('figures/electricity_consumption/'+figure_name+'_'+str(which_house)+'.pdf')
	

	
	
	#plt.savefig('figures/electricity_consumption/'+figure_name+'_'+str(which_house)+'.eps', format='eps', dpi=1000)
	#plt.savefig('figures/electricity_consumption/'+figure_name+'_'+str(which_house)+'.png', format='png', dpi=1000)
	