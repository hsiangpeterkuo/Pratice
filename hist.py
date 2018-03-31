#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 21:48:47 2018

@author: emily
"""

import numpy as np
import matplotlib.pyplot as plt
plt.subplot(2,2,1)
n_groups = 8 

c = np.loadtxt('/Users/emily/.spyder-py3/cost 0.4 20.txt')   
M = c[0] 
R = c[1]
L = c[2]
T = c[3]      
index = np.arange(n_groups)  
bar_width = 0.25  
       
opacity = 0.4  
rects1 = plt.bar(index+bar_width, L,bar_width,alpha=opacity, color='k',label=    'L',hatch = '///',ls = ':')  
rects2 = plt.bar(index + 2*bar_width, M, bar_width,alpha=opacity,color='#888888', hatch = '',label='M')  
rects3 = plt.bar(index, R, bar_width,alpha=opacity, color='#000000',label=  'R')
plt.xlabel('Coalitions')  
plt.ylabel('Standard error = 20',fontweight='bold')  
plt.title('p = 0.4',fontweight='bold')  
plt.xticks(index + bar_width, ('MLR', '(M)RL', 'MR(L)', 'M(R)L', '(ML)R','(MR)L','M(RL)','(MRL)'),fontsize = 9)  
plt.ylim(0,30000)
plt.legend(loc = 'upper right')

plt.subplot(2,2,2)
n_groups = 8 

c = np.loadtxt('/Users/emily/.spyder-py3/cost 0.7 20 .txt')   
M = c[0] 
R = c[1]
L = c[2]
T = c[3]      
index = np.arange(n_groups)  
bar_width = 0.25  
       
opacity = 0.4  
rects1 = plt.bar(index+bar_width, L,bar_width,alpha=opacity, color='k',label=    'L',hatch = '///')  
rects2 = plt.bar(index + 2*bar_width, M, bar_width,alpha=opacity,color='#888888', hatch = '',label='M')  
rects3 = plt.bar(index, R, bar_width,alpha=opacity, color='#000000',label=  'R')
plt.xlabel('Coalitions')    
plt.title('p=0.7',fontweight='bold')  
plt.xticks(index + bar_width, ('MLR', '(M)RL', 'MR(L)', 'M(R)L', '(ML)R','(MR)L','M(RL)','(MRL)'),fontsize = 9)  
plt.ylim(0,30000)
plt.legend(loc = 'upper right')

plt.subplot(2,2,3)
n_groups = 8 

c = np.loadtxt('/Users/emily/.spyder-py3/cost 0.4 50.txt')   
M = c[0] 
R = c[1]
L = c[2]
T = c[3]      
index = np.arange(n_groups)  
bar_width = 0.25  
       
opacity = 0.4  
rects1 = plt.bar(index+bar_width, L,bar_width,alpha=opacity, color='k',label=    'L',hatch = '///')  
rects2 = plt.bar(index + 2*bar_width, M, bar_width,alpha=opacity,color='#888888', hatch = '',label='M')    
rects3 = plt.bar(index, R, bar_width,alpha=opacity, color='#000000',label=  'R')
plt.xlabel('Coalitions')  
plt.ylabel('Standard error = 50',fontweight='bold')  

plt.xticks(index + bar_width, ('MLR', '(M)RL', 'MR(L)', 'M(R)L', '(ML)R','(MR)L','M(RL)','(MRL)'),fontsize = 9)  
plt.ylim(0,30000)
plt.legend(loc = 'upper right')

plt.subplot(2,2,4)
n_groups = 8 

c = np.loadtxt('/Users/emily/.spyder-py3/cc.txt')   
M = c[0] 
R = c[1]
L = c[2]
T = c[3]      
index = np.arange(n_groups)  
bar_width = 0.25  
       
opacity = 0.4  
rects1 = plt.bar(index+bar_width, L,bar_width,alpha=opacity, color='k',label=    'L',hatch = '///')  
rects2 = plt.bar(index + 2*bar_width, M, bar_width,alpha=opacity,color='#888888', hatch = '',label='M')  
rects3 = plt.bar(index, R, bar_width,alpha=opacity, color='#000000',label=  'R')
plt.xlabel('Coalitions')  

plt.xticks(index + bar_width, ('MLR', '(M)RL', 'MR(L)', 'M(R)L', '(ML)R','(MR)L','M(RL)','(MRL)'),fontsize = 9)  
plt.ylim(0,30000)
plt.legend(loc = 'upper right')
    
plt.tight_layout()

plt.show()
    
