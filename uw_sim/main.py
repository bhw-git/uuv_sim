#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main.py: Main program for the Python Vehicle Simulator, which can be used
    to simulate and test guidance, navigation and control (GNC) systems.

Reference: T. I. Fossen (2021). Handbook of Marine Craft Hydrodynamics and
Motion Control. 2nd edition, John Wiley & Sons, Chichester, UK. 
URL: https://www.fossen.biz/wiley  
    
Author:     Thor I. Fossen
"""
import os
import matplotlib.pyplot as plt
from python_vehicle_simulator.vehicles import *
from python_vehicle_simulator.lib import *

# Simulation parameters: 
sampleTime = 0.02                   # sample time [seconds]
N = 10000                           # number of samples

# 3D plot and animation parameters where browser = {firefox,chrome,safari,etc.}
numDataPoints = 50                  # number of 3D data points
FPS = 10                            # frames per second (animated GIF)
filename = '3D_animation.gif'       # data file for animated GIF

###############################################################################
# Vehicle constructors
###############################################################################
printSimInfo() 

"""
remus100('depthHeadingAutopilot',z_d,psi_d,V_c,beta_c)             

Call constructors without arguments to test step inputs, e.g. DSRV(), otter(), etc. 
"""

vehicle = remus100('depthHeadingAutopilot',30,50,1525,0.5,170)     
 
printVehicleinfo(vehicle, sampleTime, N)

###############################################################################
# Main simulation loop 
###############################################################################
def main():    
    
    [simTime, simData] = simulate(N, sampleTime, vehicle)
    
    plotVehicleStates(simTime, simData, 1)                    
    plotControls(simTime, simData, vehicle, 2)
    plot3D(simData, numDataPoints, FPS, filename, 3)   
        
    plt.show()
    plt.close()

main()
