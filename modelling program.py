# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:43:54 2021

@author: gavla
"""
import argparse
#from scipy.integrate import odeint
import numpy as np
#import matplotlib.pyplot as plt
#from numpy.random import random, randint
import math

def main(*args):
    parser = argparse.ArgumentParser(description = "Model a boat's yawing motion")
    parser.add_argument('--length', metavar='N', type=int, default = 9)
    parser.add_argument('--width', metavar='N', type=int, default = 3)
    parser.add_argument('--height', metavar='N', type=int,default = 3)
    parser.add_argument('--windSpeed', metavar='N', type=int,default=0)
    parser.add_argument('--windHeading', metavar='N',type=int,default=0)
    parser.add_argument('--boatSpeed',metavar='N',type=int,default=10)
    parser.add_argument('--boatHeading',metavar='N',type=int,default=0)
    parser.add_argument('--waterSpeed',metavar='N',type=int,default=0)
    parser.add_argument('--waterHeading', metavar='N',type=int,default=0)
    parser.add_argument('--rudderAngle',metavar='N',type=int,default=0)
    parser.add_argument('--rudderLength',metavar='N',type=float,default=0.5)
    parser.add_argument('--rudderHeight',metavar='N',type=float,default=0.5)
    parser.add_argument('--density',metavar='N',type=int,default=1000)
    parser.add_argument('--boatMass',metavar='N',type=int,default=3000)
    

    args = parser.parse_args(args)
    
    force = [(args.density*args.rudderHeight*args.rudderLength*((args.boatSpeed)^2)*math.sin(args.rudderAngle)*(-math.cos(args.rudderAngle))),(args.density*args.rudderHeight*args.rudderLength*((args.boatSpeed)^2)*math.sin(args.rudderAngle)*(math.sin(args.rudderAngle))),0]
    F = np.array(force)
    radius = [-((args.length)/2+(args.rudderLength)*math.cos(args.rudderAngle)/2),-(args.rudderLength)*math.sin(args.rudderAngle)/2,0]
    R = np.array(radius)
    # torque = [0,0,args.density*args.rudderHeight*args.rudderLength*((args.boatSpeed)^2)*((math.sin(args.rudderAngle))^2)*args.rudderLength*(math.cos(args.rudderAngle)+0.5)]
    # T = np.array(torque)
    T = np.cross(F,R)
    I = (1/3)*(((args.length)^2)+((args.length)^2))*args.boatMass
    a = [0,0,T[2]/I]
    
    print(F,R,T,I,a)

# def Derivs(alpha,t,angAcc):
#     Heading=alpha
#     angAcc = torque/momInertia
#     dHeadingdt = angVel
#     dangVeldt = angAcc
import sys
main(sys.argv[1:])
    
    