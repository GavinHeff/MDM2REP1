#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Created on Mon Dec  6 18:05:28 2021

@author: freddiemarsh
"""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math

while True:
    #menu for user to choose to run with defaults or input their own parameters
    choice = input("Would you like to (a) enter values for the parameters of the system or (b) run with default values? \n")
    if choice == 'a':
        while True:
            w = width = float(input("What is the width of the boat in metres? "))
            if w < 0:
                 print("The width can not be negative.")
                 w = width = float(input("What is the width of the boat in metres? "))
            else:
                break
        while True:
            l = length = float(input("What is the length of the boat in metres? "))
            if w < 0:
                 print("The length can not be negative.")
                 l = length = float(input("What is the width of the boat in metres? "))
            else:
                break
        while True:
            v = boatspeed = float(input("What is the speed of the boat in metres per second?"))
            if v < 0:
                print("The wind speed can not be negative.")
                v = boatspeed = float(input("What is the speed of the boat in metres per second? "))
            else:
                break
        while True:
            s = rudderLength = float(input("What is the length of the rudder in metres? "))
            if s < 0:
                print("The rudder length can not be negative.")
                s = rudderLength = float(input("What is the length of the rudder in metres? "))
            else:
                break
        while True:
            rudderHeight = float(input("What is the height of the rudder in metres? "))
            if rudderHeight < 0:
                print("The rudder height can not be negative.")
                rudderHeight = float(input("What is the height of the rudder in metres? "))
            else:
                break
        while True:
            m = boatMass = float(input("What is the weight of the boat in kilogrammes? "))
            if m < 0:
                print("The weight can not be negative.")
                m = boatMass = float(input("What is the weight of the boat in kilogrammes? "))
            else:
                break
        break
    elif choice == 'b':
        l = length = 10.05 # 30 feet in metres
        width = 3.81
        v = 10
        rudderLength = 0.5
        rudderHeight = 0.5
        boatMass = 2437,5
        break
    else:
        print("Entry must be 'a' or 'b'")
        
filename = str(input("Enter a name for the plot file to be saved under"))

#defining other constants
rho = density = 1000 # density of water
h = 1 #submerged 'draught' height of boat
k1 = 1/18 # lower values decrease peak angular velocity
k2 = 0.1 # higher values result in longer time to stabilise - maximum value depends on other parameters
C1 = -1
C2 = -1


#calculating values based on given constants
A = Area = rudderLength*rudderHeight # Area of rudder
D = k2*l**3*h*rho/64 #drag coefficient
RudderForceConstant = 3*k1*rho*A*(v**2)*l/2
I = (1/3)*(((length)**2)+((width)**2))*boatMass 
print([D,RudderForceConstant])


def Derivs(x,t):
    #defining the system of ODEs to be solved
    angVel = x[0] #angular velocity of the boat (radians per second)
    alpha = x[1] #angular position of the boat (radians)
    
    

    beta = (C1*alpha + C2*angVel) #angular position of the rudder (radians)
    if beta > math.radians(35):
        beta = math.radians(35)
    elif beta < -math.radians(35):
        beta = -math.radians(35)
    else:
        beta = beta
    dangVeldt=(RudderForceConstant*(math.sin(beta))-D*angVel**2)/I  #2nd order DE for angular acceleration in terms of angular velocity and angular position
    dalphadt = angVel #equating first derivative of angular position to angular velocity
    
    
    return [dangVeldt,dalphadt]
    
x0 = [0.1,math.radians(80)]#set initial conditions

"""
WORKING CONDITIONS FROM TRIAL AND ERROR
Works when initial alpha < 85 and initia velocity = 1
    Works for any angle if vAng0 = 0
    Converges faster depending on surge velocity as expected
    works best when RudderAngleConstant = 10 * D 

"""
"""
ANALYSIS TO FIND OPTIMAL C1 AND C2
    #Stability anaysis. IF C1 C2 too big its unstable. if too small will take ages to converge
    # If lambda is real, stable if lambda<0
    #If complex, look at real part of the root, same as above
    #as long as real part of solution <0 it will stabilise
    #look for critical damping which is a repeated root
    """

    

ts = np.linspace(0,100,100)#timespan for model, 15s with 100 steps
solution = odeint(Derivs, x0, ts)#use odeint model to numerically solve ODE

#display results on plot
heading = solution[:,1]
angularVelocity = solution[:,0]
rudderAngle = C1*solution[:,1] + C2*solution[:,0]
rudderAngle[rudderAngle > math.radians(35)] = math.radians(35)
rudderAngle[rudderAngle < math.radians(-35)] = math.radians(-35)
plt.plot(ts,heading,'b-',label='Alpha(radians)')
plt.plot(ts,angularVelocity,'r-',label='Angular Velocity (radians/s)')
plt.plot(ts,rudderAngle,'g-',label = 'Beta (radians)')
plt.legend(loc='best')
plt.xlabel('Time (s)')
plt.ylabel('Alpha, Beta, Angular velocity of ship')
plt.title('Graph of motion over time')
plt.grid(True)
plt.savefig("figs/"+filename+".pdf")
plt.show()