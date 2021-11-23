# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:43:54 2021

@author: gavla
"""
import argparse
import numpy as np
import matplotlin.pyplot as plt
from numpy.random import random, randint

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
    parser.add_argument('--density',metavar='N',type=int,default=30)