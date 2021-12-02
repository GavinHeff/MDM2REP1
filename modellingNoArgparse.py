# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 17:29:51 2021

@author: gavla
"""
import numpy as np
from scipy.integrate import odeint
import math
import matplotlib.pyplot as plt

length = 9
width = 3
height = 3
windSpeed = 0
windHeading = 0
boatSpeed=10
boatHeading=0
waterSpeed=0
waterHeading=0
rudderAngle=35
rudderLength=0.5
rudderHeight=0.5
density=1000
boatMass=3000


force = [(density*rudderHeight*rudderLength*(boatSpeed)**2)*math.sin(rudderAngle)*(-math.cos(rudderAngle)),(density*rudderHeight*rudderLength*((boatSpeed)**2)*math.sin(rudderAngle)*(math.sin(rudderAngle))),0]
F = np.array(force)
radius = [-((length)/2+(rudderLength)*math.cos(rudderAngle)/2),-(rudderLength)*math.sin(rudderAngle)/2,0]
R = np.array(radius)
# torque = [0,0,args.density*args.rudderHeight*args.rudderLength*((args.boatSpeed)^2)*((math.sin(args.rudderAngle))^2)*args.rudderLength*(math.cos(args.rudderAngle)+0.5)]
# T = np.array(torque)
T = np.cross(F,R)
I = (1/3)*(((length)**2)+((length)**2))*boatMass
a = [0,0,T[2]/I]

print(F,R,T,I,a)

def Derivs(t, x):
    Alpha = x[0]
    d2Alphadt2 = a
    return[d2Alphadt2]

Alpha0 = 0

x0 = [Alpha0]
print(Derivs(x=x0, t=0))

tr = np.linspace(0,10,1000)
solution = odeint(Derivs,x0,tr)

Alpha = solution[:,0]

plt.plot(tr,Alpha,'b',label='Boat Heading')
plt.legend(loc='best')
plt.title('Change in boat heading against time')
plt.xlabel('Time, secs')
plt.ylabel('Boat heading')
plt.grid(True)
plt.show

dangveldt = (3*density*rudderHeight*rudderLength*(boatSpeed**2)*((math.sin(rudderAngle))**2)*rudderLength*math.cos(rudderAngle)+length/2)/((length**2 + width**2)*boatMass)
print(dangveldt/2)