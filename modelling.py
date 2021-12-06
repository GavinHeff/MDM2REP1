from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import minimize


l = length = 9.144 # 30 feet in metres
rho = density = 1000 # density of water
D = 1 #drag coefficient
k = 1
C = math.pi**2
w = 3
v = 10
#beta = 0
s = 0.5
rudderLength = 0.5
rudderHeight = 0.5
boatMass = 3000

# while True:
#     w = width = float(input("What is the width of the boat in metres: "))
#     if w < 0:
#         print("The width can not be negative.")
#         w = width = float(input("What is the width of the boat in metres: "))
#     else:
#         break
#     break

# while True:
#     v = boatspeed = float(input("What is the speed of the boat: "))
#     if v < 0:
#         print("The wind speed can not be negative.")
#         v = boatspeed = float(input("What is the speed of the boat: "))
#     else:
#         break
#     break

# while True:
#     beta = rudderAngle = float(input("What is the angle of the rudder in degrees: "))
#     if abs(beta) > 90:
#         print("The rudder angle can't be bigger than 90 degrees")
#         beta = rudderAngle = float(input("What is the angle of the rudder in degrees: "))
#     else:
#         break
#     break

# while True:
#     s = rudderLength = float(input("What is the length of the rudder: "))
#     if s < 0:
#         print("The rudder length can not be negative.")
#         s = rudderLength = float(input("What is the length of the rudder: "))
#     else:
#         break
#     break

# while True:
#     rudderHeight = float(input("What is the height of the rudder: "))
#     if rudderHeight < 0:
#         print("The rudder height can not be negative.")
#         rudderHeight = float(input("What is the height of the rudder: "))
#     else:
#         break
#     break

# while True:
#     m = boatMass = float(input("What is the weight of the boat: "))
#     if m < 0:
#         print("The weight can not be negative.")
#         m = boatMass = float(input("What is the weight of the boat: "))
#     else:
#         break
#     break

# pi = math.pi 
A = Area = rudderLength*rudderHeight # Area of rudder
# Izz = 1/3 * m * (l**2 + w**2) # Second moment of area for a cuboid

def Derivs(x,t):
    # force = [(density*rudderHeight*rudderLength*(v)**2)*math.sin(beta)*(-math.cos(beta)),(density*rudderHeight*rudderLength*((v)**2)*math.sin(beta)*(math.sin(beta))),0]
    # F = np.array(force)
    # radius = [-((length)/2+(rudderLength)*math.cos(beta)/2),-(rudderLength)*math.sin(beta)/2,0]
    # R = np.array(radius)
    #T = np.cross(F,R)
    I = (1/3)*(((length)**2)+((length)**2))*boatMass 
    
    beta = C*x[0]
    
    dy1dt = x[0]
    dy2dt=-(D*x[0]/I) - (3*k*rho*A*(v**2)*(math.sin(beta)**2)*(s*math.cos(beta)+l/2))/I
    print(dy1dt, dy2dt)
    return [dy1dt, dy2dt]
    
x0 = [5,math.radians(50)]

#print(Derivs(x0,0))
    


ts = np.linspace(1,10,100)
xs = odeint(Derivs, x0, ts)
print(xs)
ys = xs[:,0]
plt.plot(ts,xs,'-')
plt.plot(ts,ys,'r-')
plt.xlabel('Time/s')
plt.ylabel('Heading/degrees')
plt.title('Heading change with time')
plt.grid(True)
plt.show()

# x=90  

# t=0
# k=1
# #ts = np.linspace(1,10,1000)
# ts = []
# xs = []
# bs = []
# #xs = odeint(Derivs, x0, t)
# for t in range(0,30):
#     ts.append(t)
#     xs.append(x)
#     #t+=0.1
#     bs.append(beta)
#     if not t%2:
#         if x < -50:
#             beta-=10
#             x += ((3*k*rho*A*(v**2)*(math.sin(x)**2))*(s*math.cos(beta)+l/2)*(t**2)) / (2*m*(l**(2)+w**(2)))
#         elif x > 50:
#             beta+=1
#             x -= ((3*k*rho*A*(v**2)*(math.sin(x)**2))*(s*math.cos(beta)+l/2)*(t**2)) / (2*m*(l**(2)+w**(2)))
#         elif x < -20:
#             beta-=0.5
#             x -= ((3*k*rho*A*(v**2)*(math.sin(x)**2))*(s*math.cos(beta)+l/2)*(t**2)) / (2*m*(l**(2)+w**(2)))
#         elif x > 20:
#             beta+=0.5
#             x -= ((3*k*rho*A*(v**2)*(math.sin(x)**2))*(s*math.cos(beta)+l/2)*(t**2)) / (2*m*(l**(2)+w**(2)))
#         elif x < -10:
#             beta-=0.1
#             x -= ((3*k*rho*A*(v**2)*(math.sin(x)**2))*(s*math.cos(beta)+l/2)*(t**2)) / (2*m*(l**(2)+w**(2)))
#         elif x > 10:
#             beta+=0.1
#             x -= ((3*k*rho*A*(v**2)*(math.sin(x)**2))*(s*math.cos(beta)+l/2)*(t**2)) / (2*m*(l**(2)+w**(2)))
     
#print(xs,ts)



# #ys = xs[:,0]
# plt.plot(ts,xs,'-')
# plt.plot(ts,bs,'r-')
# plt.xlabel('Time/s')
# plt.ylabel('Heading, rudder angle/degrees')
# plt.title('Heading and rudder angle change with time')
# plt.show()




