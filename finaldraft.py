from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import minimize

pi = math.pi 
l = length = 9.144 # 30 feet in metres
rho = density = 1000 # density of water
h = 2
k = 1/100
C1 = 1
C2 = 1
w = 3
v = 10
#beta = 0
s = 0.2
rudderLength = 0.5
rudderHeight = 0.5
boatMass = 3000
A = Area = rudderLength*rudderHeight # Area of rudder
D = l*h*rho #drag coefficient
RudderForceConstant = 3*k*rho*A*(v**2)


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

# Izz = 1/3 * m * (l*2 + w*2) # Second moment of area for a cuboid

def Derivs(x,t):
    angVel = x[0]
    alpha = x[1]
   
    
    I = (1/3)*((length**2)+((length)**2))*boatMass 
    
    # if alpha > 0:
    #     f = -1
    # else:
    #     f = 1

    beta = (C1*alpha + C2*angVel)
    #PD conrol
    
    # if alpha > 0:
    #     beta = -1
    # else:
    #     beta = 1
    # #bang-bang control
    
    # dangVeldt=-(D*angVel*2*l/I) + (3*k*rho*A(v*2)(math.sin(beta)*2)(s*math.cos(beta)+l/2))/I
    # #dangVeldt original equation
    
    
    # dangVeldt=(D*angVel*2*l/I) - (3*k*rho*A(v*2)*beta(l/2))/I
    # #dangVeldt without trig terms
    
    dangVeldt=angVel**2-beta
    #dangVeldt without trig terms or any variables
    
    
    
    
    dalphadt = angVel
    
    
    return [dangVeldt,dalphadt]
    
x0 = [1,math.radians(90)]

#print(Derivs(x0,t=1))
    


ts = np.linspace(0,50,100)
solution = odeint(Derivs, x0, ts)
# print(solution)


heading = solution[:,1]
angularVelocity = solution[:,0]
# print(solution[:,0])
# print(solution[:,1]) 
plt.plot(ts,heading,'bx-',label='Heading')
plt.plot(ts,angularVelocity,'r-',label='Angular Velocity')
plt.legend(loc='best')
plt.xlabel('Time (s)')
plt.ylabel('Heading displacement, angualar velocity')
plt.title('Heading change with time')
plt.grid(True)
plt.show()


"""POTENTIAL ISSUES

1. Graph plot is not consistent. Why? I dont change te variables yet the plot changes. 
Mega irregularities like spikes in heading that cant be rectified without negative velocity. 
Theres rarely negative velocity.

2. Maybe doesnt like trig terms

3. WHAT IS THIS:
        /opt/anaconda3/lib/python3.8/site-packages/scipy/integrate/odepack.py:247: ODEintWarning: 
        Excess work done on this call (perhaps wrong Dfun type).
        Run with full_output = 1 to get quantitative information.
        warnings.warn(warning_msg, ODEintWarning)

entered  'full_output=1'
returned new error:
    'message': 'Excess work done on this call (perhaps wrong Dfun type).'})
"""