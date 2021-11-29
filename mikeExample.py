# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 15:22:24 2021

@author: gavla
"""

# ODE for Bucket in Python
# mass is hung from spring in some oil, which gives drag force against motion

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# BASIC IDEAS
# Model idea is: net inflow (Litres/s) accumulates in a Bucket(as Litres)
# Can extend this idea to other physical, chemical systems:
# force over time on moveable Mass accumulates as momentum: Mom=INTEGRAL(Force)
# from momentum calculate velocity :                     Vel=Mom/Mass
# velocity accumulates over time as distance:            Dis=INTEGRAL(Vel)
# the Momentum representing the kinetic energy   and
# the Distance (representing potential energy) define the 'State'  of the system

# Define the parameters for this model,
# they will be available inside the key Derivs function which follows
Mass=10 #Kg
Ks  =100 #N/m, stiffness of spring,
g   =9.81 # m/s2  accelerarion due to gravity
Drag=10 # N/(m/s), is proportioanl to velocity

# DEFINE the inputs to the INTEGRATORS in the form of a list of derivatives
# this is defining the derivative function, i.e rates of change of state.
# You can think of of the 'Derivs' as the net flows which acumulate.
def Derivs( x,t ):  # x is the 'state vector', t is current value of time
    # assign names to elements of state vector
    Mom=x[0]
    Dis=x[1]
    #DEFINE the actual equations
    Vel= Mom/Mass
    #Net force downwards
    Fdown= Mass*g- Ks*Dis - Drag*Vel
    dMomdt = Fdown
    dDisdt = Vel
    return [dMomdt,dDisdt]

# Define initial conditions for t=0
# this one starts with Dis=0 and Mom=0 because Vel=0
Mom0=0
Dis0=0
x0=[Mom0,Dis0]

# can check the work so far, just as the mass sets off downwards...
print( Derivs(x=x0,t=0 ))

# SOLVE the Differential equations by doing numerical integrations, 
# define the time range and call on the odeint() function to do the work:
tr=np.linspace(0,10,1000) # from 0 to 10 with 1000 intermediate data points.
solution=odeint(Derivs,x0,tr) # here's where all the 'solving' is done.

# extract the results:
Mom=solution[:,0]
Vel=Mom/Mass
Dis=solution[:,1]

#print(Mom/4.2)
#print(Dis)

#plot the results
plt.plot(tr,Vel,'b',label='Velocity')
plt.plot(tr,Dis,'r',label='Distance')
plt.legend(loc='best')
plt.title('Mass, Spring moving in oil')
plt.xlabel('Time, secs')
plt.ylabel('Vel, Distance')
plt.grid(True)
plt.show()


      