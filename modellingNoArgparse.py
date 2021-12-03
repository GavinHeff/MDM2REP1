# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 16:35:07 2021

@author: gavla
"""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math

length = 9
width = 3
height = 3
windSpeed = 0
windHeading = 0
boatSpeed=10
boatHeading=0
waterSpeed=0
waterHeading=0
rudderAngle=-20
rudderLength=0.5
rudderHeight=0.5
density=1000
boatMass=3000

l = length
w = width
h = height
v = boatSpeed
beta = rudderAngle
s = rudderLength
A = rudderLength*rudderHeight
rho = density
m = boatMass

def Derivs(x,t):
    # boatAngVel=x[0]
    # alpha = x[1]
    
    ode = x[0] - (3*rho*A*v**2*(math.sin(beta)**2)*(math.sin(beta)+l/2))/(m*(l**2+w**2))
    return(ode)    
    
    # force = [(density*rudderHeight*rudderLength*(boatSpeed)**2)*math.sin(rudderAngle)*(-math.cos(rudderAngle)),(density*rudderHeight*rudderLength*((boatSpeed)**2)*math.sin(rudderAngle)*(math.sin(rudderAngle))),0]
    # F = np.array(force)
    # radius = [-((length)/2+(rudderLength)*math.cos(rudderAngle)/2),-(rudderLength)*math.sin(rudderAngle)/2,0]
    # R = np.array(radius)
    # T = np.cross(F,R)#
    # I = (1/3)*(((length)**2)+((length)**2))*boatMass
    # a = [0,0,T[2]/I]   
    
    # d2Alphadt2 = a[2]

x0 = [0]
ts = np.linspace(1,10,1000)
xs = odeint(Derivs, x0, ts)
ys = xs[:,0]
plt.plot(ts,xs,'-')
plt.plot(ts,ys,'r*')
plt.xlabel('Time/s')
plt.ylabel('Heading/degrees')
plt.title('Heading change with time')
plt.show


