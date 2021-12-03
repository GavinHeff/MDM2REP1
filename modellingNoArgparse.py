from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math

l = length = 9.144 # 30 feet in metres
rho = density = 1000 # density of water


while True:
    w = width = int(input("What is the width of the boat in metres: "))
    if w < 0:
        print("The width can not be negative.")
        w = width = int(input("What is the width of the boat in metres: "))
    else:
        break
    break

while True:
    v = boatspeed = int(input("What is the speed of the boat: "))
    if v < 0:
        print("The wind speed can not be negative.")
        v = boatspeed = int(input("What is the speed of the boat: "))
    else:
        break
    break

while True:
    beta = rudderAngle = int(input("What is the angle of the rudder in degrees: "))
    if abs(beta) > 90:
        print("The rudder angle can't be bigger than 90 degrees")
        beta = rudderAngle = int(input("What is the angle of the rudder in degrees: "))
    else:
        break
    break

while True:
    s = rudderLength = int(input("What is the length of the rudder: "))
    if s < 0:
        print("The rudder length can not be negative.")
        s = rudderLength = int(input("What is the length of the rudder: "))
    else:
        break
    break

while True:
    rudderHeight = int(input("What is the height of the rudder: "))
    if rudderHeight < 0:
        print("The rudder height can not be negative.")
        rudderHeight = int(input("What is the height of the rudder: "))
    else:
        break
    break

while True:
    m = boatMass = int(input("What is the weight of the boat: "))
    if m < 0:
        print("The weight can not be negative.")
        m = boatMass = int(input("What is the weight of the boat: "))
    else:
        break
    break

pi = math.pi 
A = Area = rudderLength*rudderHeight # Area of rudder
Izz = 1/3 * m * (l^2 + w^2) # Second moment of area for a cuboid

def Derivs(x,t):
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


